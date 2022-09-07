from django.shortcuts import render, redirect
from .models import Product, Order, Customer
from .forms import OrderForm

def dashboard(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()
    total_order = orders.count()
    deliver = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context={
        'orders': orders,
        'customer': customer,
        'total_order': total_order,
        'deliver': deliver,
        'pending': pending,

    }
    return render(request, 'm_dashboard/dashboard.html',  context)


def product(request):
    item = Product.objects.all()
    context={
        'item': item
    }
    return render(request, 'm_dashboard/product.html')



def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    order = customer.order_set.all()
    order_count = order.count()

    context = {
        'pk_test': pk_test,
        'customer': customer,
        'order': order,
        'order_count': order_count
    }
    return render(request, 'm_dashboard/customer.html', {'pk_test':pk_test})

def createOrder(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'm_dashboard/order_create.html', context)

def updateOrder(request, pk):
    order = Order.object.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'm_dashboard/order_create.html', context)

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {
        'order': order
    }
    return render(request, 'm_dashboard/delete.html', context)