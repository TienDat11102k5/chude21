from django.shortcuts import render,redirect,get_object_or_404
from home.forms import Pet,PetForm,Customer,CustomerForm,Employee,EmployeeForm,Veterinarian,VeterinarianForm
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home/hom9.html')
def index(request):
    return render(request, 'index.html')

#Quản lý thú cưng
def customer_list(request):
    return render(request, 'customer_list.html')
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'QL_DS_THU_CUNG/customer_list.html', {'customers': customers})
def pet_management(request, customer_id):
    customer = get_object_or_404(Customer, customer_id=customer_id)
    pets = Pet.objects.filter(customer_id=customer_id) 
    return render(request, 'QL_DS_THU_CUNG/quan-ly-thu-cung.html', {'customer': customer, 'pets': pets})
def delete_pet(request, pet_id):
    pet = get_object_or_404(Pet, pet_id=pet_id)
    pet.delete()
    return redirect('pet_management', customer_id=pet.customer.customer_id)
def success(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            new_pet = form.save(commit=False)
            new_pet.customer = form.cleaned_data.get('customer')
            new_pet.save()
            return redirect('pet_management', customer_id=new_pet.customer.customer_id) 
    else:
        form = PetForm()
    customers = Customer.objects.all()
    return render(request, 'QL_DS_THU_CUNG/success.html', {'form': form, 'customers': customers})
#Quản lý thú cưng

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

#Quản Lý Khách Hàng
def kh_list(request):
    customers = Customer.objects.all()
    return render(request, 'QL_Khach_Hang/ds-khach-hang.html', {'customers': customers})

def create_customer_account(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ds-khach-hang')
        else:
            print(form.errors)
    else:
        form = CustomerForm()
    return render(request, 'QL_Khach_Hang/tao-tai-khoan-khach-hang.html', {'form': form})

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.delete()
    return redirect('ds-khach-hang') 

#Quản Lý Khách Hàng

# Quản lý nhân viên
def nv_list(request):
    employees = Employee.objects.all()
    return render(request, 'QL_Nhan_Vien/ds-nhan-vien.html', {'employees': employees})

def create_employee_account(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ds-nhan-vien')
        else:
            print(form.errors)
    else:
        form = EmployeeForm()
    return render(request, 'QL_Nhan_Vien/tao-tai-khoan-nhan-vien.html', {'form': form})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.delete()
    return redirect('ds-nhan-vien') 
# Quản lý nhân viên

def create_doctor_account(request):
    return render(request, 'tao-tai-khoan-bac-si.html')
def system_configuration(request):
    return render(request, 'cau-hinh-he-thong.html')
def activity_statistics(request):
    return render(request, 'thong-ke-hoat-dong.html')