from django.urls import path
from . import views

urlpatterns = [
    path('', views.veterinarian_list, name='veterinarian_list'),
    path('<int:veterinarian_id>/', views.veterinarian_detail, name='veterinarian_detail'),
    path('create/', views.veterinarian_create, name='veterinarian_create'),
    path('<int:veterinarian_id>/edit/', views.veterinarian_update, name='veterinarian_update'),
    path('<int:veterinarian_id>/delete/', views.veterinarian_delete, name='veterinarian_delete'),
]
