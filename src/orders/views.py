from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm
from .models import Order
# Create your views here.


def home_view(request, *args, **kwargs):
    queryset = Order.objects.all()
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        "form": form,
        "object_list": queryset
    }
    return render(request, "home.html", context)


def detail_view(request, id, *args, **kwargs):
    queryset = get_object_or_404(Order, id=id)

    context = {
        "item": queryset
    }
    return render(request, "order.html", context)


def delete_view(request, id, *args, **kwargs):
    Order.objects.filter(id=id).delete()
    queryset = Order.objects.all()
    return redirect('../../')
