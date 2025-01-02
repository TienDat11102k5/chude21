from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import TreatmentRecord

# View để hiển thị danh sách hồ sơ điều trị
def treatment_record_list(request):
    treatment_records = TreatmentRecord.objects.all()
    return render(request, 'treatment_record_list.html', {'treatment_records': treatment_records})

# View để hiển thị chi tiết của một hồ sơ điều trị
def treatment_record_detail(request, record_id):
    treatment_record = get_object_or_404(TreatmentRecord, pk=record_id)
    return render(request, 'treatment_record_detail.html', {'treatment_record': treatment_record})

# View để tạo một hồ sơ điều trị mới
def treatment_record_create(request):
    if request.method == 'POST':
        pet_id = request.POST.get('pet_id')
        veterinarian_id = request.POST.get('veterinarian_id')
        diagnosis = request.POST.get('diagnosis')
        prescriptions = request.POST.get('prescriptions')
        notes = request.POST.get('notes')
        treatment_record = TreatmentRecord.objects.create(pet_id=pet_id, veterinarian_id=veterinarian_id, diagnosis=diagnosis, prescriptions=prescriptions, notes=notes)
        return HttpResponse("TreatmentRecord created successfully")
    return render(request, 'treatment_record_form.html')

# View để cập nhật thông tin của một hồ sơ điều trị
def treatment_record_update(request, record_id):
    treatment_record = get_object_or_404(TreatmentRecord, pk=record_id)
    if request.method == 'POST':
        treatment_record.pet_id = request.POST.get('pet_id')
        treatment_record.veterinarian_id = request.POST.get('veterinarian_id')
        treatment_record.diagnosis = request.POST.get('diagnosis')
        treatment_record.prescriptions = request.POST.get('prescriptions')
        treatment_record.notes = request.POST.get('notes')
        treatment_record.save()
        return HttpResponse("TreatmentRecord updated successfully")
    return render(request, 'treatment_record_form.html', {'treatment_record': treatment_record})

# View để xóa một hồ sơ điều trị
def treatment_record_delete(request, record_id):
    treatment_record = get_object_or_404(TreatmentRecord, pk=record_id)
    treatment_record.delete()
    return HttpResponse("TreatmentRecord deleted successfully")
