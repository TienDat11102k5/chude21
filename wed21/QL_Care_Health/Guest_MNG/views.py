from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Guest

# View để hiển thị danh sách khách
def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'guest_list.html', {'guests': guests})

# View để hiển thị thông tin chi tiết của một khách
def guest_detail(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)
    return render(request, 'guest_detail.html', {'guest': guest})

# View để tạo một khách mới
def guest_create(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        address = request.POST.get('address')
        name = request.POST.get('name')
        email = request.POST.get('email')
        guest = Guest.objects.create(user_id=user_id, address=address, name=name, email=email)
        return HttpResponse("Guest created successfully")
    return render(request, 'guest_form.html')

# View để cập nhật thông tin của một khách
def guest_update(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)
    if request.method == 'POST':
        guest.user_id = request.POST.get('user_id')
        guest.address = request.POST.get('address')
        guest.name = request.POST.get('name')
        guest.email = request.POST.get('email')
        guest.save()
        return HttpResponse("Guest updated successfully")
    return render(request, 'guest_form.html', {'guest': guest})

# View để xóa một khách
def guest_delete(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)
    guest.delete()
    return HttpResponse("Guest deleted successfully")
