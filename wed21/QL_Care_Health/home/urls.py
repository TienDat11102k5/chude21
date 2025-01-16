from django.contrib import admin
from django.urls import include, path
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('index.html', views.index, name='index'),
    
    path('customer_list.html', views.customer_list, name='customer_list'),
    path('quan-ly-thu-cung.html/<int:customer_id>/', views.pet_management, name='pet_management'),
    path('customer_list/quan-ly-thu-cung.html/<int:customer_id>/', views.customer_list, name='customer_list'),
    path('success.html', views.success, name='success'),
    path('delete_pet/<int:pet_id>/', views.delete_pet, name='delete_pet'),
    
    
    path('lich-su-kham.html', views.examination_history, name='history_exam'),
    path('dang-ky-kham.html', views.dang_ky_kham_view, name='register_exam'),
    path('checkin-thu-cung.html', views.checkin_thu_cung_view, name='checkin_pet'),
    path('danh-gia-kham.html', views.danh_gia_kham_view, name='evaluate_exam'),
    path('theo-doi-nhap-vien.html', views.theo_doi_nhap_vien_view, name='track_admission'),
    path('quan-ly-booking.html', views.quan_ly_booking_view, name='manage_booking'),
    path('quan-ly-chuong.html', views.quan_ly_chuong_view, name='manage_kennel'),
    path('cap-nhat-thong-tin-chuong.html', views.cap_nhat_thong_tin_chuong_view, name='update_kennel'),
    path('sap-lich-kham.html', views.sap_lich_kham_view, name='schedule_exam'),
    path('sap-lich-nhap-vien.html', views.sap_lich_nhap_vien_view, name='schedule_admission'),
    path('thoi-gian-kham.html', views.thoi_gian_kham_view, name='exam_time'),
    path('ghi-nhan-kham.html', views.ghi_nhan_kham_view, name='record_exam'),
    path('cham-soc-nhap-vien.html', views.cham_soc_nhap_vien_view, name='care_admission'),


    path('ds-khach-hang.html', views.kh_list, name='ds-khach-hang'),
    path('tao-tai-khoan-khach-hang.html', views.create_customer_account, name='create_customer_account'),
    path('customers/delete/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    
    path('tao-tai-khoan-nhan-vien.html', views.create_employee_account, name='create_employee_account'),
    path('tao-tai-khoan-bac-si.html', views.create_doctor_account, name='create_doctor_account'),
    path('cau-hinh-he-thong.html', views.system_configuration, name='system_configuration'),
    path('thong-ke-hoat-dong.html', views.activity_statistics, name='activity_statistics'),
]
