from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_list, name='role_list'),
    path('<int:role_id>/', views.role_detail, name='role_detail'),
    path('create/', views.role_create, name='role_create'),
    path('<int:role_id>/edit/', views.role_update, name='role_update'),
    path('<int:role_id>/delete/', views.role_delete, name='role_delete'),
]
