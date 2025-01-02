from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Service

# View để hiển thị danh sách dịch vụ
def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})

# View để hiển thị chi tiết của một dịch vụ
def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'service_detail.html', {'service': service})

# View để tạo một dịch vụ mới
def service_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        Service.objects.create(name=name, description=description, price=price)
        return HttpResponse("Service created successfully")
    return render(request, 'service_form.html')

# View để cập nhật thông tin của một dịch vụ
def service_update(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        service.name = request.POST.get('name')
        service.description = request.POST.get('description')
        service.price = request.POST.get('price')
        service.save()
        return HttpResponse("Service updated successfully")
    return render(request, 'service_form.html', {'service': service})

# View để xóa một dịch vụ
def service_delete(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    return HttpResponse("Service deleted successfully")
