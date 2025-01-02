from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Veterinarian

# View để hiển thị danh sách các bác sĩ thú y
def veterinarian_list(request):
    veterinarians = Veterinarian.objects.all()
    return render(request, 'veterinarian_list.html', {'veterinarians': veterinarians})

# View để hiển thị thông tin chi tiết của một bác sĩ thú y
def veterinarian_detail(request, veterinarian_id):
    veterinarian = get_object_or_404(Veterinarian, pk=veterinarian_id)
    return render(request, 'veterinarian_detail.html', {'veterinarian': veterinarian})

# View để tạo một bác sĩ thú y mới
def veterinarian_create(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        specialization = request.POST.get('specialization')
        veterinarian = Veterinarian.objects.create(user_id=user_id, specialization=specialization)
        return HttpResponse("Veterinarian created successfully")
    return render(request, 'veterinarian_form.html')

# View để cập nhật thông tin của một bác sĩ thú y
def veterinarian_update(request, veterinarian_id):
    veterinarian = get_object_or_404(Veterinarian, pk=veterinarian_id)
    if request.method == 'POST':
        veterinarian.user_id = request.POST.get('user_id')
        veterinarian.specialization = request.POST.get('specialization')
        veterinarian.save()
        return HttpResponse("Veterinarian updated successfully")
    return render(request, 'veterinarian_form.html', {'veterinarian': veterinarian})

# View để xóa một bác sĩ thú y
def veterinarian_delete(request, veterinarian_id):
    veterinarian = get_object_or_404(Veterinarian, pk=veterinarian_id)
    veterinarian.delete()
    return HttpResponse("Veterinarian deleted successfully")
