from django.urls import path
from . import views

urlpatterns = [
    path('Customer_MNG', views.Customer, name='Customer_MNG'),
]