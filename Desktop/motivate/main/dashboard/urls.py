from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # dashboard
    path('', views.index, name='index'),

    # customer pages
    path('createCustomer/', views.createCustomer, name='createCustomer'),
    path('customer-list/', views.customerList, name='customerList'),
    path('customer/<str:pk_id>/', views.customerPage, name='customerPage'),
    path('customer/<str:pk_id>/paymentdetail/', views.customerPaymentList, name='customerPaymentList'),
    path('customer/<str:pk_id>/customer-property-list/', views.customerPropertyList, name='customerPropertyList'),
    
    # property pages
    path('propertyList/', views.propertyList, name='propertyList'),
    path('create-property-page/', views.createProperty, name='createProperty'),
    path('property-details/<str:pk_id>/', views.propertydetails, name='propertydetails'),

    # for purchases
    path('payment-list/', views.paymentpage, name='paymentpage'),

    # Documents
    path('customer/<str:pk_id>/openCustomerReceipt/', views.receipts, name='receipts'),
    path('download/<str:pk_id>/openCustomerReceipt/', views.downloadreceipt, name='downloadreceipt'),
    
    # message
    path('customer/<str:pk_id>/message', views.sendMessage, name='sendMessage'),
    path('customer/<str:pk_id>/whatappMessage', views.whatappMessage),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   