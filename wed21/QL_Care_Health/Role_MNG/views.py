from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Role

# View để hiển thị danh sách các vai trò
def role_list(request):
    roles = Role.objects.all()
    return render(request, 'role_list.html', {'roles': roles})

# View để hiển thị chi tiết của một vai trò
def role_detail(request, role_id):
    role = get_object_or_404(Role, pk=role_id)
    return render(request, 'role_detail.html', {'role': role})

# View để tạo một vai trò mới
def role_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        role = Role.objects.create(name=name, description=description)
        return HttpResponse("Role created successfully")
    return render(request, 'role_form.html')

# View để cập nhật thông tin của một vai trò
def role_update(request, role_id):
    role = get_object_or_404(Role, pk=role_id)
    if request.method == 'POST':
        role.name = request.POST.get('name')
        role.description = request.POST.get('description')
        role.save()
        return HttpResponse("Role updated successfully")
    return render(request, 'role_form.html', {'role': role})

# View để xóa một vai trò
def role_delete(request, role_id):
    role = get_object_or_404(Role, pk=role_id)
    role.delete()
    return HttpResponse("Role deleted successfully")
