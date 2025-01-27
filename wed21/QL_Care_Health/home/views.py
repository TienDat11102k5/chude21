from django.shortcuts import render,redirect,get_object_or_404
from home.forms import Pet,PetForm,Customer,CustomerForm,Employee,EmployeeForm
from home.forms import Veterinarian, VeterinarianForm,LichTrinhBS,LichTrinhBSForm,Booking,BookingForm
from django.http import HttpResponseForbidden
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



def customer_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.status = 'Pending'
            booking.save()
            messages.success(request, 'Lịch đặt đã được tạo thành công!')
            return redirect('customer_booking')
    else:
        form = BookingForm()

    customers = Customer.objects.all()
    bookings = Booking.objects.filter(customer__in=customers)
    return render(request, 'Booking/dang-ky-kham.html', {'form': form, 'bookings': bookings})

def customer_cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if booking.status != 'Pending':
        messages.error(request, 'Lịch đặt không thể hủy.')
    else:
        booking.cancel_booking(cancelled_by_customer=True)
        messages.success(request, 'Bạn đã hủy lịch đặt thành công.')
    
    return redirect('customer_booking')



def quan_ly_booking_view(request):
    bookings = Booking.objects.all()
    veterinarians = Veterinarian.objects.all()
    return render(request, 'Booking/quan-ly-booking.html', {'bookings': bookings, 'veterinarians': veterinarians})

def employee_cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.status != 'Pending':
        messages.error(request, 'Lịch đặt không thể hủy.')
    else:
        booking.cancel_booking(cancelled_by_employee=True)
        messages.success(request, f'Nhân viên đã hủy lịch đặt ID {booking_id} thành công.')
    return redirect('quan_ly_booking')

def change_veterinarian(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    veterinarians = Veterinarian.objects.all()
    if request.method == "POST":
        veterinarian_id = request.POST.get('veterinarian')
        if veterinarian_id:
            try:
                veterinarian = get_object_or_404(Veterinarian, id=veterinarian_id)
                booking.veterinarian = veterinarian
                booking.save()
                messages.success(request, "Cập nhật bác sĩ thành công!")
            except Exception as e:
                messages.error(request, f"Lỗi khi cập nhật bác sĩ: {e}")
        else:
            messages.error(request, "Vui lòng chọn bác sĩ trước khi cập nhật.")
        return redirect('quan_ly_booking')

    return render(request, 'change_veterinarian.html', {
        'booking': booking,
        'veterinarians': veterinarians
    })

def employee_change_booking_status(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if not request.user.has_perm('Booking.change_booking_status'):  # Kiểm tra quyền truy cập
        return HttpResponseForbidden("Bạn không có quyền chỉnh sửa trạng thái.")
    if request.method == 'POST':
        new_status = request.POST.get('status')  # Lấy trạng thái mới từ POST
        if new_status in ['Pending', 'Confirmed', 'Cancelled']:
            booking.status = new_status  # Cập nhật trạng thái của booking
            # Nếu trạng thái là 'Confirmed' và chưa có bác sĩ, yêu cầu chọn bác sĩ
            if new_status == 'Confirmed' and not booking.veterinarian:
                veterinarian_id = request.POST.get('veterinarian')
                if veterinarian_id:
                    veterinarian = get_object_or_404(Veterinarian, id=veterinarian_id)
                    booking.veterinarian = veterinarian  # Gán bác sĩ cho lịch đặt
                else:
                    # Nếu không có bác sĩ được chọn, tự động gán bác sĩ đầu tiên trong danh sách
                    default_veterinarian = Veterinarian.objects.first()
                    if default_veterinarian:
                        booking.veterinarian = default_veterinarian
            booking.save()  # Lưu thay đổi vào cơ sở dữ liệu
            messages.success(request, f"Trạng thái lịch đặt ID {booking.id} đã được cập nhật thành công!")
        else:
            messages.error(request, "Trạng thái không hợp lệ.")
    return redirect('quan_ly_booking')

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, f'Lịch đặt ID {booking_id} đã được xóa thành công.')
    return redirect('quan_ly_booking')

def checkin_thu_cung_view(request):
    return render(request, 'checkin-thu-cung.html')
def danh_gia_kham_view(request):
    return render(request, 'danh-gia-kham.html')
def theo_doi_nhap_vien_view(request):
    return render(request, 'theo-doi-nhap-vien.html')

def quan_ly_chuong_view(request):
    return render(request, 'quan-ly-chuong.html')
def cap_nhat_thong_tin_chuong_view(request):
    return render(request, 'cap-nhat-thong-tin-chuong.html')
def sap_lich_kham_view(request):
    return render(request, 'sap-lich-kham.html')
def sap_lich_nhap_vien_view(request):
    return render(request, 'sap-lich-nhap-vien.html')

#Đăng ký lịch trình bác sĩ
def lichDK_list(request):
    veterinarians = Veterinarian.objects.all()  # Lấy tất cả bác sĩ
    data = []
    for vet in veterinarians:
        lich_trinh_list = vet.lich_trinh.all()  # Lấy tất cả lịch khám của bác sĩ
        data.append({
            'veterinarian': vet,
            'lich_trinh_list': lich_trinh_list
        })
    return render(request, 'BS_DK_Lich/lich-dang-ky.html', {'data': data})

def thoi_gian_kham_view(request, veterinarian_id):
    veterinarian = get_object_or_404(Veterinarian, pk=veterinarian_id)
    if request.method == 'POST':
        form = LichTrinhBSForm(request.POST)
        if form.is_valid():
            lich_trinh = form.save(commit=False)
            lich_trinh.veterinarian = veterinarian
            lich_trinh.save()
            return redirect('lichDK_list')
    else:
        form = LichTrinhBSForm()
    return render(request, 'BS_DK_Lich/thoi-gian-kham.html', {'form': form, 'veterinarian': veterinarian})

def delete_lichDK(request, lich_trinh_id):
    lich_trinh = LichTrinhBS.objects.filter(id=lich_trinh_id).first()
    if lich_trinh:
        lich_trinh.delete()
    return redirect('lichDK_list')

#Đăng ký lịch trình bác sĩ


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



#Quản lý nhân viên
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
#Quản lý nhân viên



# Quản lý bác sĩ
def bs_list(request):
    veterinarians= Veterinarian.objects.all()
    return render(request, 'QL_Bac_Si/ds-bac-si.html', {'veterinarians': veterinarians})

def create_doctor_account(request):
    if request.method == 'POST':
        form = VeterinarianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ds-bac-si')
        else:
            print(form.errors)
    else:
        form = VeterinarianForm()
    return render(request, 'QL_Bac_Si/tao-tai-khoan-bac-si.html', {'form': form})

def delete_veterinarian(request, veterinarian_id):
    employee = get_object_or_404(Employee, pk=veterinarian_id)
    employee.delete()
    return redirect('ds-bac-si') 
# Quản lý bác sĩ


def system_configuration(request):
    return render(request, 'cau-hinh-he-thong.html')
def activity_statistics(request):
    return render(request, 'thong-ke-hoat-dong.html')