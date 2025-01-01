from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employee

# View để hiển thị danh sách các nhân viên
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

# View để hiển thị thông tin chi tiết của một nhân viên
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'employee_detail.html', {'employee': employee})

# View để tạo một nhân viên mới
def employee_create(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        specialization = request.POST.get('specialization')
        employee = Employee.objects.create(user_id=user_id, specialization=specialization)
        return HttpResponse("Employee created successfully")
    return render(request, 'employee_form.html')

# View để cập nhật thông tin của một nhân viên
def employee_update(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.user_id = request.POST.get('user_id')
        employee.specialization = request.POST.get('specialization')
        employee.save()
        return HttpResponse("Employee updated successfully")
    return render(request, 'employee_form.html', {'employee': employee})

# View để xóa một nhân viên
def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.delete()
    return HttpResponse("Employee deleted successfully")
