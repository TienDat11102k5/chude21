from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('<int:service_id>/', views.service_detail, name='service_detail'),
    path('create/', views.service_create, name='service_create'),
    path('<int:service_id>/edit/', views.service_update, name='service_update'),
    path('<int:service_id>/delete/', views.service_delete, name='service_delete'),
]
