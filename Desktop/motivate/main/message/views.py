from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import Customer


def sendMessage(request):
    
    # customer = Customer.objects.all(id=pk_id)

    return render(request, 'home.html')



# def whatappData(phonenumber, message):
#     import time
#     import webbrowser as web
#     import pyautogui as pg
#     web.open('https://web.whatsapp.com/send?phone='+phonenumber+'&text='+message )
#     time.sleep(30)
#     pg.press('enter')


def sendMesage(request, pk_id):
    customer = Customer.objects.all(id=pk_id)
    
    friendsnumber = '+234' + customer.phoneNumber


    if request.method == 'POST':
        # phonenumber = request.POST['phone']
        phonenumber = eachnumber
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

        return render(request, 'home.html', {'msg': msg})

    else:
        return HttpResponse("<h1>404 - Error in form submission :- ... </h1>")