from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User

# View để hiển thị danh sách người dùng
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

# View để hiển thị chi tiết của một người dùng
def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user_detail.html', {'user': user})

# View để tạo một người dùng mới
def user_create(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        birthdate = request.POST.get('birthdate')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        role_id = request.POST.get('role_id')
        User.objects.create(fullname=fullname, birthdate=birthdate, gender=gender, phone=phone, email=email, role_id=role_id)
        return HttpResponse("User created successfully")
    return render(request, 'user_form.html')

# View để cập nhật thông tin của một người dùng
def user_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.fullname = request.POST.get('fullname')
        user.birthdate = request.POST.get('birthdate')
        user.gender = request.POST.get('gender')
        user.phone = request.POST.get('phone')
        user.email = request.POST.get('email')
        user.role_id = request.POST.get('role_id')
        user.save()
        return HttpResponse("User updated successfully")
    return render(request, 'user_form.html', {'user': user})

# View để xóa một người dùng
def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return HttpResponse("User deleted successfully")
