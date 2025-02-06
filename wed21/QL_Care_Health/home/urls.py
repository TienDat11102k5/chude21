from django.contrib import admin
from django.urls import include, path
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('index.html', views.index, name='index'),
    # Quản lý Thú Cưng
    path('customer_list.html', views.customer_list, name='customer_list'),
    path('quan-ly-thu-cung.html/<int:customer_id>/', views.pet_management, name='pet_management'),
    path('customer_list/quan-ly-thu-cung.html/<int:customer_id>/', views.customer_list, name='customer_list'),
    path('success.html', views.success, name='success'),
    path('delete_pet/<int:pet_id>/', views.delete_pet, name='delete_pet'),
     # Quản lý Thú Cưng
#-------------------------------------------------------------------------------------------------------------#
    
    
    
    
    
    
    
    path('lich-su-kham.html', views.examination_history, name='history_exam'),







#-------------------------------------------------------------------------------------------------------------#
    #BookingBooking

    path('dang-ky-kham.html', views.customer_booking, name='customer_booking'),
    path('cancel_booking/<int:booking_id>/', views.customer_cancel_booking, name='customer_cancel_booking'),
    path('quan-ly-booking.html', views.quan_ly_booking_view, name='quan_ly_booking'),
    path('employee/cancel-booking/<int:booking_id>/', views.employee_cancel_booking, name='employee_cancel_booking'),
    path('booking/<int:booking_id>/change-status/', views.employee_change_booking_status, name='employee_change_booking_status'),
    path('booking/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
    path('change-veterinarian/<int:booking_id>/', views.change_veterinarian, name='employee_change_veterinarian'),
    path('cancel-booking/<int:booking_id>/', views.customer_cancel_booking, name='customer_cancel_booking'),

  #BookingBooking
#-------------------------------------------------------------------------------------------------------------#





    path('ghi-nhan-kham.html', views.ghi_nhan_kham_view, name='record_exam'),
    path('lich-su-kham.html', views.examination_history, name='lich_su_kham'),
    path('danh-gia-kham/<int:record_id>.html', views.rating_view, name='danh_gia_kham'),
    path('danh-gia-chua-danh-gia.html', views.rating_pending_view, name='danh_gia_chua_danh_gia'),
    path('danh-sach-cho-xep-chuong.html', views.danh_sach_cho_xep_chuong, name='danh_sach_cho_xep_chuong'),
    path('gan-chuong/', views.assign_kennel, name='gan_chuong'),
    path('quan-ly-chuong.html', views.quan_ly_chuong_view, name='quan-ly-chuong'),
    path('xoa-chuong/<int:kennel_id>/', views.xoa_chuong, name='xoa_chuong'),
    path('quan-ly-chuong.html', views.quan_ly_chuong_view, name='quan_ly_chuong'),
    path('reset_kennel/<int:kennel_id>/', views.reset_kennel, name='reset_kennel'),


    
    path('checkin-thu-cung.html', views.checkin_thu_cung_view, name='checkin_pet'),
    
   
    
  
    path('sap-lich-kham.html', views.sap_lich_kham_view, name='schedule_exam'),





    path('sap-lich-nhap-vien.html', views.sap_lich_nhap_vien_view, name='schedule_admission'),
    path('theo-doi-nhap-vien.html', views.theo_doi_nhap_vien_view, name='track_admission'),
    path('danh-sach-cham-soc.html',views.danh_sach_cham_soc_view, name='danh_sach_cham_soc'),
    path('cap-nhat-cham-soc/<int:record_id>/',views.cap_nhat_cham_soc_view, name='cap_nhat_cham_soc'),
    path('xoa-cham-soc/<int:record_id>/', views.xoa_cham_soc_view, name='xoa_cham_soc'),



    
    path('lich-dang-ky.html', views.lichDK_list, name='lichDK_list'),
    path('thoi-gian-kham.html', views.thoi_gian_kham_view, name='exam_time'),
    path('thoi-gian-kham/<int:veterinarian_id>/', views.thoi_gian_kham_view, name='exam_time'),
    path('delete_lichDK/<int:lich_trinh_id>/', views.delete_lichDK, name='delete_lichDK'),



   
    
#-------------------------------------------------------------------------------------------------------------#
    # tài khoản khách hàng
    path('ds-khach-hang.html', views.kh_list, name='ds-khach-hang'),
    path('tao-tai-khoan-khach-hang.html', views.create_customer_account, name='create_customer_account'),
    path('customers/delete/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    # tài khoản khách hàng

#-------------------------------------------------------------------------------------------------------------#
   
   
    # tài khoản nhân viên
    path('ds-nhan-vien.html', views.nv_list, name='ds-nhan-vien'),
    path('tao-tai-khoan-nhan-vien.html', views.create_employee_account, name='create_employee_account'),
    path('employees/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    # tài khoản nhân viên

#-------------------------------------------------------------------------------------------------------------#
    
    
    # tài khoản bác sỹ
    path('ds-bac-si.html', views.bs_list, name='ds-bac-si'),
    path('tao-tai-khoan-bac-si.html', views.create_doctor_account, name='create_doctor_account'),
    path('veterinarians/delete/<int:veterinarian_id>/', views.delete_veterinarian, name='delete_veterinarian'),
    # tài khoản bác sỹ

#-------------------------------------------------------------------------------------------------------------#

    path('cau-hinh-he-thong.html', views.system_configuration, name='system_configuration'),
    path('thong-ke-hoat-dong.html', views.activity_statistics, name='activity_statistics'),
]
