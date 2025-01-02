from django.urls import path
from . import views

urlpatterns = [
    path('', views.guest_list, name='guest_list'),
    path('<int:guest_id>/', views.guest_detail, name='guest_detail'),
    path('create/', views.guest_create, name='guest_create'),
    path('<int:guest_id>/edit/', views.guest_update, name='guest_update'),
    path('<int:guest_id>/delete/', views.guest_delete, name='guest_delete'),
]
