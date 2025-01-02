from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pet

# View để hiển thị danh sách thú cưng
def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pet_list.html', {'pets': pets})

# View để hiển thị thông tin chi tiết của một thú cưng
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'pet_detail.html', {'pet': pet})

# View để tạo một thú cưng mới
def pet_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        species = request.POST.get('species')
        age = request.POST.get('age')
        medical_history = request.POST.get('medical_history')
        customer_id = request.POST.get('customer_id')
        pet = Pet.objects.create(name=name, species=species, age=age, medical_history=medical_history, customer_id=customer_id)
        return HttpResponse("Pet created successfully")
    return render(request, 'pet_form.html')

# View để cập nhật thông tin của một thú cưng
def pet_update(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    if request.method == 'POST':
        pet.name = request.POST.get('name')
        pet.species = request.POST.get('species')
        pet.age = request.POST.get('age')
        pet.medical_history = request.POST.get('medical_history')
        pet.customer_id = request.POST.get('customer_id')
        pet.save()
        return HttpResponse("Pet updated successfully")
    return render(request, 'pet_form.html', {'pet': pet})

# View để xóa một thú cưng
def pet_delete(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    pet.delete()
    return HttpResponse("Pet deleted successfully")
