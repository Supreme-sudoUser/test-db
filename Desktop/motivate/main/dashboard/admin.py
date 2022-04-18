from django.contrib import admin

from .models import Customer, Property, Purchase, Payment

admin.site.register(Customer)
admin.site.register(Property)
admin.site.register(Purchase)   
admin.site.register(Payment)
