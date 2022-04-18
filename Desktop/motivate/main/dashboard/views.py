from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# for page data filter
from .filters import *

# Import Pagination
from django.core.paginator import Paginator
 
# pdfgeneration for receipt and documents
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa
 
# Dashboard Page
@login_required
def index(request):
    customer = Customer.objects.all()
    properties = Property.objects.all()
    purchase = Purchase.objects.all()
    payment = Payment.objects.all()

    balance = 0
    allPayment = 0
    # get all purchases
    if customer:
        for eachPurchase in purchase:
            balance += eachPurchase.actual_payment
            
        for eachPayment in payment:
            allPayment += eachPayment.depositpayment



        # for i in balance:
        #     # i+=i
        #     balance = int(i)

    total_customers = customer.count()
    context = {
        'customer': customer,
        'total_customers': total_customers,
        'balance': balance,
        'allPayment': allPayment,
        'properties': properties,
    }

    return render(request, 'pages/dashboardpage.html', context)

def staffPage(request):
    return render(request, 'pages/staff/staff-page.html')

def createStaff(request):
    return render(request, 'pages/staff/create-staff.html')


# for customers======================================================================================

# All customer pages inherit from customerSelf
def customerSelf(r, pk_id):
    customer = Customer.objects.get(id=pk_id)
    purchaseItem = customer.purchase_set.all()
    

    context = {
        'customer': customer,
        'purchaseItem': purchaseItem,
    }
    return render(r, 'pages/customer/customer.html', context)

# create customer here
@login_required
def createCustomer(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = messages.info(request, 'Customer created successfully')
            return redirect('customerList')

    else:
        form = CustomerForm()

    context = {
        'form': form,
        }
    return render(request, 'pages/customer/create-customer.html', context)

# list all existing customers, pagination not active yet
@login_required
def customerList(request):
    customersName = Customer.objects.all().order_by('surname')

    myFilter = CustomerFilter(request.GET, queryset=customersName)
    customersName = myFilter.qs
    
    # import Paginator
    # p = Paginator(Customer.objects.all(), 2)
    # page = request.GET.get('page')
    # customerlist = p.get_page('page')

    #</for the template>
    #   {% if customerlist.has_previous %}
    #                     <a href="?page=1">&laquo; First</a> |
    #                     <a href="?page={{ customerlist.previous_page_number }}">previous</a>
    #                 {% endif %}

    #                 Page {{ customerlist.number }} of {{ customerlist.paginator.num_pages }}

    #                 {% if customerlist.has_next %}
    #                     <a href="?page={{customerlist.next_page_number}}">Next</a> |
    #                     <a href="?page={{customerlist.paginator.num_pages}}">Last page &raquo;</a>
                    

    #                 {% endif %}
    # </end template>

    context = {
        'customersName': customersName,
        'myFilter': myFilter,
    }

    return render(request, 'pages/customer/customer-list.html', context )

# Each customer profile page, purchase and payment history
@login_required
def customerPage(request, pk_id):
    customer = Customer.objects.get(pk=pk_id)

    return render(request, 'pages/customer/customer-page.html', {'customer': customer})

# display all property for each customer and create property 
@login_required
def customerPropertyList(request, pk_id):
    customer = Customer.objects.get(id=pk_id)
    purchaseItem = customer.orders.all()
    if purchaseItem:
        for purchase in purchaseItem:
            # propertyItem = purchase.property 
            pass

        form = PurchaseForm(instance=purchase)
        if request.method == 'POST':
            # form = PurchaseForm(instance=purchase)
            form = PurchaseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('customerPropertyList', customer.id)
    else:
        form = PurchaseForm()
        if request.method == 'POST':
            form = PurchaseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('customerPropertyList', customer.id)

    context = {
        'form': form,
        'customer': customer,
        'purchaseItem': purchaseItem,
    }

    return render(request, 'pages/customer/customer-propertyList.html', context)


# displays customer payment history and make new payments
@login_required
def customerPaymentList(request, pk_id):
    customer = Customer.objects.get(id=pk_id)
    purchase = customer.orders.all()


    if purchase:
        for purchases in purchase:

            payment = purchases.customerpayment.all()
            if payment:
                for eachpayment in payment:
                    pass

                form = PaymentForm(instance=eachpayment)
                if request.method == 'POST':
                    form = PaymentForm(request.POST)
                    if form.is_valid():
                        form.save()
                        return redirect('customerPaymentList', customer.id)
            else:
                form = PaymentForm()
                if request.method == 'POST':
                    form = PaymentForm(request.POST)
                    if form.is_valid():
                        form.save()
                        return redirect('customerPaymentList', customer.id)
                        
    else:
        form = PaymentForm()
        if request.method == 'POST':
            form = PaymentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('customerPaymentList', customer.id)
                
    context = {
        'customer': customer,
        'purchase': purchase,
        'form': form,
    }
    return render(request, 'pages/customer/customer-paymentList.html', context)
        


#________End of Customer Pages_________________________________________________


#===========================================================================================================
# for properties

# All property pages inherits from products
@login_required
def products(request):
    products = Product.objects.all()
    pf = ProductFilter(request.GET, queryset=products)
    products = pf.qs
    return render(request,'crm/products.html',{'products':products,'pf':pf})

@login_required
def propertyList(request):
    propertyitem = Property.objects.all().order_by('name')
    context = {
        'propertyitem' : propertyitem,
    }

    return render(request, 'pages/property/property-List.html', context)

@login_required
def propertydetails(request, pk_id):
    properties = Property.objects.get(id=pk_id)
    purchase = properties.purchase_set.all()
    customer = Customer.objects.all()
    context = {
        'purchase': purchase,
        'properties': properties,
        'customer': customer
    }

    return render(request, 'pages/property/property-Page.html', context)
    
@login_required
def createProperty(request):

    form = PropertyForm()

    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('propertyList')
    else:
        context = {
            'form' : form
        }
    
    return render(request, 'pages/property/create-property.html', context)
 

#================================Purchases=============================================================================

@login_required
def purchaseList(request):
    purchase = Purchase.objects.all()
    filtersid = purchase.filter()

    context = {
        'purchase': purchase,
        'filtersid': filtersid,
    }
    return render(request, 'pages/purchase/all-purchases.html', context)


# ============

@login_required
def paymentpage(request):
    payment = Payment.objects.all().order_by('-date_created')


    myFilter = PaymentFilter(request.GET, queryset=payment)
    payment = myFilter.qs
    

    context = {
        'payment': payment,
        'myFilter': myFilter,
    }
    return render(request, 'pages/payment/payment.html', context)

# ============receipts and documents==================
def receipts(request, pk_id, *args, **kwargs):
    payment = Payment.objects.get(id=pk_id)

    context = {
        'payment': payment,
    }
    return render(request, 'documents/receipt.html', context)


# To be activated
def downloadreceipt(request, pk_id):
    payment = Payment.objects.get(id=pk_id)
    template_path = 'documents/receipt.html'
    context = {
        'payment': payment,
    }

    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition'] = 'filename="receipt.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('Something is wrong somewhere' + html + '</pre')
    return response
    

def downloadR(request, pk_id):
    payment = Payment.objects.get(id=pk_id)
    template_path = 'documents/receipt2.html'
    context = {
        'payment': payment,
    }

    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition'] = 'attachment: filename="receipt.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('Something is wrong somewhere' + html + '</pre')
    return response
    
# ============================================================================
# ============================================================================

def sendMessage(request, pk_id):
    customer = Customer.objects.get(id=pk_id)
    return render(request, 'documents/message.html', {'customer': customer})

def whatappMessage(request, pk_id):
    
    customer = Customer.objects.get(id=pk_id)


    if request.method == 'POST':
        # phonenumber = request.POST['phone']

        friendsnumber =  customer.phoneNumber[1 : : ]
    
        phonenumber = '+234' + friendsnumber
        print(friendsnumber)
        print(phonenumber)

        message = request.POST['message']
        print(phonenumber, message)
        msg = "Message Has Been Sent..."

        
        def whatappData(phonenumber, message):
            import time
            import webbrowser as web
            import pyautogui as pg
            web.open('https://web.whatsapp.com/send?phone='+phonenumber+'&text='+message )
            time.sleep(30)
            pg.press('enter')
            time.sleep(10)
            
        whatappData(phonenumber, message)

        return redirect('customerPage', customer.id)
        # return render(request, 'home.html', {'msg': msg})

    else:
        msg = "<h1>404 - Error in form submission :- ... </h1>"
        return redirect('customerList')
