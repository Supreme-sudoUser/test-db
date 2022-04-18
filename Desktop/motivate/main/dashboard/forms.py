from django.forms import ModelForm
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        
class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


