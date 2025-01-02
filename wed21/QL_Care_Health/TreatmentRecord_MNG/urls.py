from django.urls import path
from . import views

urlpatterns = [
    path('', views.treatment_record_list, name='treatment_record_list'),
    path('<int:record_id>/', views.treatment_record_detail, name='treatment_record_detail'),
    path('create/', views.treatment_record_create, name='treatment_record_create'),
    path('<int:record_id>/edit/', views.treatment_record_update, name='treatment_record_update'),
    path('<int:record_id>/delete/', views.treatment_record_delete, name='treatment_record_delete'),
]
