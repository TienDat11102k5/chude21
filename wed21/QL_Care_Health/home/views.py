from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def home(request):
    return render(request, 'home/hom9.html')
def index(request):
    return render(request, 'index.html')
def pet_management(request):
    return render(request, 'quan-ly-thu-cung.html')
def examination_history(request):
    return render(request, 'lich-su-kham.html')
def dang_ky_kham_view(request):
    return render(request, 'dang-ky-kham.html')
def checkin_thu_cung_view(request):
    return render(request, 'checkin-thu-cung.html')
def danh_gia_kham_view(request):
    return render(request, 'danh-gia-kham.html')
def theo_doi_nhap_vien_view(request):
    return render(request, 'theo-doi-nhap-vien.html')
def quan_ly_booking_view(request):
    return render(request, 'quan-ly-booking.html')
def quan_ly_chuong_view(request):
    return render(request, 'quan-ly-chuong.html')
def cap_nhat_thong_tin_chuong_view(request):
    return render(request, 'cap-nhat-thong-tin-chuong.html')
def sap_lich_kham_view(request):
    return render(request, 'sap-lich-kham.html')
def sap_lich_nhap_vien_view(request):
    return render(request, 'sap-lich-nhap-vien.html')
def thoi_gian_kham_view(request):
    return render(request, 'thoi-gian-kham.html')
def ghi_nhan_kham_view(request):
    return render(request, 'ghi-nhan-kham.html')
def cham_soc_nhap_vien_view(request):
    return render(request, 'cham-soc-nhap-vien.html')
def create_customer_account(request):
    return render(request, 'tao-tai-khoan-khach-hang.html')
def create_employee_account(request):
    return render(request, 'tao-tai-khoan-nhan-vien.html')
def create_doctor_account(request):
    return render(request, 'tao-tai-khoan-bac-si.html')
def system_configuration(request):
    return render(request, 'cau-hinh-he-thong.html')
def activity_statistics(request):
    return render(request, 'thong-ke-hoat-dong.html')