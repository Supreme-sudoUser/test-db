from django.urls import path
from . import views


urlpatterns = [
    # login/sign-up/recover
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('logout/', views.logout, name='logout'),
]