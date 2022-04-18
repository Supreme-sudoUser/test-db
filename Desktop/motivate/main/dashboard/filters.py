import django_filters
from django_filters import CharFilter
from django_filters import DateFilter
from .models import *

class CustomerFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='dateRegistered', lookup_expr='gte')
    end_date = DateFilter(field_name='dateRegistered', lookup_expr='lte')
    
    class Meta:
        model = Customer
        fields = ['surname', 'gender']
        # fields = '__all__'


class PaymentFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    
    class Meta:
        model = Payment
        # fields = ['purchase__customer']
        fields = '__all__'

