from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Appointment

# View để hiển thị danh sách cuộc hẹn
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

# View để hiển thị thông tin chi tiết của một cuộc hẹn
def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'appointment_detail.html', {'appointment': appointment})

# View để tạo một cuộc hẹn mới
def appointment_create(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        pet_id = request.POST.get('pet_id')
        veterinarian_id = request.POST.get('veterinarian_id')
        date = request.POST.get('date')
        time = request.POST.get('time')
        status = request.POST.get('status')
        notes = request.POST.get('notes')
        appointment = Appointment.objects.create(customer_id=customer_id, pet_id=pet_id, veterinarian_id=veterinarian_id, date=date, time=time, status=status, notes=notes)
        return HttpResponse("Appointment created successfully")
    return render(request, 'appointment_form.html')

# View để cập nhật thông tin của một cuộc hẹn
def appointment_update(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        appointment.customer_id = request.POST.get('customer_id')
        appointment.pet_id = request.POST.get('pet_id')
        appointment.veterinarian_id = request.POST.get('veterinarian_id')
        appointment.date = request.POST.get('date')
        appointment.time = request.POST.get('time')
        appointment.status = request.POST.get('status')
        appointment.notes = request.POST.get('notes')
        appointment.save()
        return HttpResponse("Appointment updated successfully")
    return render(request, 'appointment_form.html', {'appointment': appointment})

# View để xóa một cuộc hẹn
def appointment_delete(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.delete()
    return HttpResponse("Appointment deleted successfully")
