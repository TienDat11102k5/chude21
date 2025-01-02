from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Customer

# View để hiển thị danh sách khách hàng
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

# View để hiển thị thông tin chi tiết của một khách hàng
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'customer_detail.html', {'customer': customer})

# View để tạo một khách hàng mới
def customer_create(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        address = request.POST.get('address')
        customer = Customer.objects.create(user_id=user_id, address=address)
        return HttpResponse("Customer created successfully")
    return render(request, 'customer_form.html')

# View để cập nhật thông tin của một khách hàng
def customer_update(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        customer.user_id = request.POST.get('user_id')
        customer.address = request.POST.get('address')
        customer.save()
        return HttpResponse("Customer updated successfully")
    return render(request, 'customer_form.html', {'customer': customer})

# View để xóa một khách hàng
def customer_delete(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.delete()
    return HttpResponse("Customer deleted successfully")
