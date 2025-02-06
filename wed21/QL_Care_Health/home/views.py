from django.shortcuts import render,redirect,get_object_or_404
from home.forms import Pet,PetForm,Customer,CustomerForm,Employee,EmployeeForm,Kennel, KennelAssignment,AssignKennelForm,KennelForm
from home.forms import Veterinarian, VeterinarianForm,LichTrinhBS,LichTrinhBSForm,Booking,BookingForm,MedicalRecord,MedicalRecordForm,MedicalRecordRatingForm
from home.forms import ScheduleAdmissionForm,CareAdmissionForm,HospitalizationRecord
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.db.models import Sum
from django.utils.timezone import now
from datetime import timedelta


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

def checkin_thu_cung_view(request):
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
    return render(request, 'QL_DS_THU_CUNG/checkin-thu-cung.html', {'form': form, 'customers': customers})
#Quản lý thú cưng




#Booking
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
        messages.error(request, 'Lịch đặt không thể hủy. Trạng thái hiện tại không phải Pending.')
    else:
        booking.status = 'Cancelled'
        booking.save()
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
    if not request.user.has_perm('Booking.change_booking_status'):
        return HttpResponseForbidden("Bạn không có quyền chỉnh sửa trạng thái.")
    if request.method == 'POST':
        new_status = request.POST.get('status') 
        if new_status in ['Pending', 'Confirmed', 'Cancelled']:
            booking.status = new_status 
            if new_status == 'Confirmed' and not booking.veterinarian:
                veterinarian_id = request.POST.get('veterinarian')
                if veterinarian_id:
                    try:
                        veterinarian = get_object_or_404(Veterinarian, id=veterinarian_id)
                        booking.veterinarian = veterinarian
                    except Exception as e:
                        messages.error(request, f"Lỗi khi cập nhật bác sĩ: {e}")
                else:
                    default_veterinarian = Veterinarian.objects.first()
                    if default_veterinarian:
                        booking.veterinarian = default_veterinarian
                    else:
                        messages.error(request, "Không có bác sĩ nào được chọn và không có bác sĩ mặc định.")
                        return redirect('quan_ly_booking')
            if new_status == 'Confirmed':
                booking.paid = True  
            booking.save()  
            messages.success(request, f"Trạng thái lịch đặt ID {booking.id} đã được cập nhật thành công!")
        else:
            messages.error(request, "Trạng thái không hợp lệ.")
    
    return redirect('quan_ly_booking')
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, f'Lịch đặt ID {booking_id} đã được xóa thành công.')
    return redirect('quan_ly_booking')
#Booking


def danh_gia_kham_view(request):
    return render(request, 'danh-gia-kham.html')


#theo doi
def sap_lich_nhap_vien_view(request):
    if request.method == "POST":
        form = ScheduleAdmissionForm(request.POST)
        if form.is_valid():
            assignment = form.save()
            kennel = assignment.kennel
            kennel.is_occupied = True
            kennel.save()
            HospitalizationRecord.objects.create(pet=assignment.pet, kennel_assignment=assignment)
            return redirect('track_admission')
    else:
        form = ScheduleAdmissionForm()
    return render(request, 'Theo_doi/sap-lich-nhap-vien.html', {'form': form})


def theo_doi_nhap_vien_view(request):
    records = HospitalizationRecord.objects.filter(discharged_at__isnull=True)
    return render(request, 'Theo_doi/theo-doi-nhap-vien.html', {'records': records})


def danh_sach_cham_soc_view(request):
    records = HospitalizationRecord.objects.filter(discharged_at__isnull=True)
    return render(request, 'Theo_doi/danh-sach-cham-soc.html', {'records': records})


def cap_nhat_cham_soc_view(request, record_id):
    record = get_object_or_404(HospitalizationRecord, record_id=record_id)
    if request.method == "POST":
        form = CareAdmissionForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_cham_soc')
    else:
        form = CareAdmissionForm(instance=record)
    return render(request, 'Theo_doi/cap-nhat-cham-soc.html', {'form': form, 'record': record})

def xoa_cham_soc_view(request, record_id):
    record = get_object_or_404(HospitalizationRecord, record_id=record_id)
    record.delete()
    return redirect('danh_sach_cham_soc')

#theo doi


#Đăng ký lịch trình bác sĩ
def sap_lich_kham_view(request):
    veterinarians = Veterinarian.objects.all()
    data = []
    for vet in veterinarians:
        lich_trinh_list = vet.lich_trinh.all()
        data.append({
            'veterinarian': vet,
            'lich_trinh_list': lich_trinh_list
        })
    return render(request, 'sap-lich-kham.html', {'data': data})

def lichDK_list(request):
    veterinarians = Veterinarian.objects.all()
    data = []
    for vet in veterinarians:
        lich_trinh_list = vet.lich_trinh.all()
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
    veterinarian= get_object_or_404(Veterinarian, pk=veterinarian_id)
    veterinarian.delete()
    return redirect('ds-bac-si') 
# Quản lý bác sĩ


#--------------------------------------------------------------------------------------------------------#

def ghi_nhan_kham_view(request):
    if request.method == "POST":
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lich_su_kham')
    else:
        form = MedicalRecordForm()
    return render(request, 'Ho_So_Kham/ghi-nhan-kham.html', {'form': form})

def examination_history(request):
    records = MedicalRecord.objects.all().order_by('-date')
    return render(request, 'Ho_So_Kham/lich-su-kham.html', {'records': records})


def rating_view(request, record_id):
    record = get_object_or_404(MedicalRecord, pk=record_id)
    
    if request.method == 'POST':
        form = MedicalRecordRatingForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('lich_su_kham')
    else:
        form = MedicalRecordRatingForm(instance=record)

    return render(request, 'Ho_So_Kham/danh-gia-kham.html', {'form': form, 'record': record})

def rating_pending_view(request):
    records = MedicalRecord.objects.filter(rating__isnull=True).order_by('-date')
    return render(request, 'Ho_So_Kham/danh-gia-chua-danh-gia.html', {'records': records})


def danh_sach_cho_xep_chuong(request):
    pets_needing_kennel = MedicalRecord.objects.filter(stay_required=True).values_list('pet', flat=True)
    assigned_pets = KennelAssignment.objects.values_list('pet', flat=True)
    unassigned_pets = [pet for pet in pets_needing_kennel if pet not in assigned_pets]
    available_kennels = Kennel.objects.filter(is_occupied=False)

    unassigned_pets = [Pet.objects.get(pk=pet) for pet in unassigned_pets]
    kennel_info = []
    for kennel in available_kennels:
        pet_name = None
        kennel_assignment = KennelAssignment.objects.filter(kennel=kennel).first()
        if kennel_assignment and kennel_assignment.pet:
            pet_name = kennel_assignment.pet.name
        kennel_info.append({'kennel': kennel, 'pet_name': pet_name})

    return render(request, 'Ho_So_Kham/danh-sach-cho-xep-chuong.html', {
        'unassigned_pets': unassigned_pets,
        'available_kennels': available_kennels,
        'kennel_info': kennel_info
    })

def assign_kennel(request):
    if request.method == "POST":
        form = AssignKennelForm(request.POST)
        if form.is_valid():
            assignment = form.save()
            kennel = assignment.kennel
            kennel.is_occupied = True
            kennel.save()
            pet = assignment.pet
            medical_record = MedicalRecord.objects.filter(pet=pet).first()
            if medical_record:
                medical_record.stay_required = True 
                medical_record.save()

            return redirect('danh_sach_cho_xep_chuong')
    else:
        form = AssignKennelForm()
    return render(request, 'Ho_So_Kham/gan-chuong.html', {'form': form})

def quan_ly_chuong_view(request):
    kennels = Kennel.objects.all()
    form = KennelForm()
    kennel_info = []
    for kennel in kennels:
        pet_name = None
        kennel_assignment = KennelAssignment.objects.filter(kennel=kennel).first()
        if kennel_assignment and kennel_assignment.pet:
            pet_name = kennel_assignment.pet.name
        kennel_info.append({'kennel': kennel, 'pet_name': pet_name})
    if request.method == 'POST':
        form = KennelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quan-ly-chuong')

    return render(request, 'Ho_So_Kham/quan-ly-chuong.html', {'form': form, 'kennels': kennels, 'kennel_info': kennel_info})

def xoa_chuong(request, kennel_id):
    kennel = get_object_or_404(Kennel, kennel_id=kennel_id)
    kennel.delete()
    return redirect('quan_ly_chuong')

def reset_kennel(request, kennel_id):
    try:
        kennel = Kennel.objects.get(pk=kennel_id)
    except Kennel.DoesNotExist:
        messages.error(request, 'Chuồng không tồn tại.')
        return redirect('quan_ly_chuong')
    if kennel.is_occupied:
        kennel.is_occupied = False
        kennel_assignment = KennelAssignment.objects.filter(kennel=kennel).first()
        if kennel_assignment:
            pet = kennel_assignment.pet
            medical_record = MedicalRecord.objects.filter(pet=pet).first()
            if medical_record:
                medical_record.stay_required = False
                medical_record.save()
            kennel_assignment.pet = None
            kennel_assignment.save()
        kennel.save()
        messages.success(request, 'Chuồng đã được làm trống và không có thú cưng.')
    else:
        messages.info(request, 'Chuồng đã trống và không có thú cưng.')
    return redirect('danh_sach_cho_xep_chuong') 
#--------------------------------------------------------------------------------------------------------#



def system_configuration(request):
    return render(request, 'cau-hinh-he-thong.html')



def activity_statistics(request):
    bookings = Booking.objects.filter(status='Confirmed', paid=True)
    today_revenue = bookings.filter(appointment_date__date=now().date()).aggregate(total=Sum('fee'))['total'] or 0
    current_month_revenue = bookings.filter(appointment_date__month=now().month, appointment_date__year=now().year).aggregate(total=Sum('fee'))['total'] or 0
    start_of_week = now() - timedelta(days=now().weekday())
    week_revenue = bookings.filter(appointment_date__gte=start_of_week).aggregate(total=Sum('fee'))['total'] or 0
    context = {
        'today_revenue': today_revenue,
        'current_month_revenue': current_month_revenue,
        'week_revenue': week_revenue,
    }
    return render(request, 'Doanh_thu/thong-ke-hoat-dong.html', context)