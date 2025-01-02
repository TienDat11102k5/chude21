from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<int:customer_id>/edit/', views.customer_update, name='customer_update'),
    path('customers/<int:customer_id>/delete/', views.customer_delete, name='customer_delete'),
]
