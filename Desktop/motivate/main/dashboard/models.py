from django.db import models

class Customer(models.Model):

    TITLE = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Others', 'Others'),
    )
    
    MARITALSTATUS = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorce', 'Divorce'),
        ('Widowed', 'Widowed'),
        ('Others', 'Others'),
    )

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )

    HEARD_ABOUT_US = (
        ('Radio Station', 'Radio Station'),
        ('Magazine', 'Magazine'),
        ('Newspaper', 'Newspaper'),
        ('Facebook', 'Facebook'),
        ('Website', 'Website'),
        ('A friend', 'A friend'),
        ('Somewhere Online', 'Somewhere Online'),
    ) 

    title = models.CharField(max_length=100, choices=TITLE, default=MARITALSTATUS[-1])
    surname = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)

    passport = models.ImageField(null=True, blank=True, upload_to="images/")

    otherName = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER, default=GENDER[-1])
    maritalstatus = models.CharField(max_length=100, choices=MARITALSTATUS, default=MARITALSTATUS[-1])
    maidenName  = models.CharField(max_length=100, null=True, blank=True)
    dateOfBirth  = models.DateField()

    email = models.EmailField(max_length=100, null=True, blank=True)
    phoneNumber = models.CharField(max_length=100, null=True, blank=True)
    homeTelephone = models.CharField(max_length=100, null=True, blank=True)
    customerHomeAddress = models.CharField(max_length=1000, null=True, blank=True)
    heard_about_us = models.CharField(max_length=100, choices=HEARD_ABOUT_US, default=HEARD_ABOUT_US[-1])
    heard_about_person = models.CharField(max_length=100, null=True, blank=True)
 
    # Next of Kin
    nk_fullName = models.CharField(max_length=100, null=True, blank=True)
    nk_telephone = models.CharField(max_length=100, null=True, blank=True)
    nk_email = models.CharField(max_length=100, null=True, blank=True)
 
    # Employment Details
    employer = models.CharField(max_length=100, null=True, blank=True)
    em_designation = models.CharField(max_length=100, null=True, blank=True)
    em_telephone = models.CharField(max_length=100, null=True, blank=True)
    em_address = models.CharField(max_length=100, null=True, blank=True)
    dateRegistered  = models.DateTimeField(auto_now_add=True, null=True)
    
    def fullname(self):
        surname = self.surname
        firstName = self.firstName
        fullname = surname + firstName
        return fullname

    def __str__(self):
        return self.title +  " " + self.surname + " " + self.firstName

class Property(models.Model): 
    name = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    location = models.CharField(max_length=500, null=True)
    quantity = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name

    # To get quantity sold remaining
    def remainQuantity(self):
        purchase = self.purchase_set.all()
        if purchase:
            totalSold = 0
            for eachpurchase in purchase:
                totalSold += int(eachpurchase.quantity)
            remain = int(self.quantity) - int(totalSold)
            return remain
        else:
            pass

    # To get total quantity sold
    def soldQuantity(self):
        purchase = self.purchase_set.all()
        if purchase:
            totalSold = 0
            for eachpurchase in purchase:
                totalSold += int(eachpurchase.quantity)
            return totalSold
        else:
            pass


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE, related_name='orders')
    propertypurchase = models.ForeignKey(Property, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    date_created  = models.DateTimeField(auto_now_add=True, null=True)
    actual_payment = models.IntegerField(default='0', null=True)

    def __str__(self):
        purchasedCustomer = str(self.customer)
        purchasedProperty = str(self.propertypurchase)
        date_createdpurchase = str(self.date_created)
        #theid = str(self.pk)
        return str(purchasedCustomer + ' for ' + purchasedProperty + ' - ' + date_createdpurchase)

    # Total paid on the purchase
    def totalPaid(self):
        payment = self.customerpayment.all()
        if payment:
            balance = 0
            for eachpayment in payment:
                balance += eachpayment.depositpayment
            return balance

    # Remaining balance on the purchase
    def balance_to_pay(self):
        payment = self.customerpayment.all()
        if payment:
            balance = 0
            for eachpayment in payment:
                balance += eachpayment.depositpayment
                totalDeposit = balance
            
            balanceToPay = self.actual_payment - totalDeposit

            return balanceToPay
        else:
            return(self.actual_payment)

    # Percent paid
    def percentPaid(self):
        payment = self.customerpayment.all()
        if payment:
            totalPaid = 0
            for eachpayment in payment:
                totalPaid += eachpayment.depositpayment
            

            x = (totalPaid * 100) / self.actual_payment
            content = str(round(x)) + '%'
            return content
        else:
            pass


    def dateStrip(self):
        date = str(self.date_created.date()).split(",", 1)[0]
        return date

class Payment(models.Model):
    PAYMENTPLAN = (
        ('outright', 'outright'),
        ('3 month installment', '3 month installment'),
        ('6 month installment', '6 month installment'),
        ('9 month installment', '9 month installment'),
        ('12 month installment', '12 month instalment'),
    )
    
    paymentplan = models.CharField(max_length=100, choices=PAYMENTPLAN, null=True)
    depositpayment = models.IntegerField(null=True)
    paymentMethod = models.CharField(max_length=100, null=True, blank=True)
    date_created  = models.DateTimeField(auto_now_add=True, null=True)
    purchase = models.ForeignKey(Purchase, null=True, on_delete=models.CASCADE, related_name='customerpayment')

    def __str__(self):
        payment = str(self.paymentplan)
        customer = str(self.purchase.customer)
        propertyPurchase = str(self.purchase.propertypurchase)
        date_created = str(self.purchase.date_created)
        payment_display = customer + ' - ' + propertyPurchase + ' - ' + date_created
        return payment_display


    def percent(self):
        depositpayment = self.depositpayment
        Actual_payment = self.purchase.actual_payment

        if depositpayment == Actual_payment:
            content = "balanced" + "100%"
            return content
        
        elif depositpayment > Actual_payment:
            overpaid = depositpayment - Actual_payment 
            content = "balance overpaid" + str(round(overpaid))
            return content

        else:
            x = (depositpayment * 100) / Actual_payment
            content = str(round(x)) + '%'
            return content

    def dateStrip(self):
        date = str(self.date_created.date()).split(",", 1)[0]
        return date
 