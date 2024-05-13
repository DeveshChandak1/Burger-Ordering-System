from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
def index(request):
    request.session.set_expiry(0)
    context = {
        'active_link': 'index',
    }
    return render(request, 'index.html')

def burger(request):
    request.session.set_expiry(0)
    burger_data = Burgers.objects.all()
    context = {
        'menu': burger_data,
        'active_link': 'burger', 
    }
    return render(request, 'burger.html', context)

def AddOn(request):
    request.session.set_expiry(0)
    AddOn_data = AddOns.objects.all()
    context = {
        'menu': AddOn_data,
        'active_link': 'AddOn',
    }
    return render(request, 'AddOn.html', context)


@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        note = request.POST.get('note')
        order_data = request.POST.get('orders')

        # Save data to Orders model
        order_instance = Orders.objects.create(note=note, order_data=order_data)
        order_instance.save()

        request.session['note'] = note
        request.session['order'] = order_data

    context = {
        'active_link': 'order',
    }
    return render(request, 'order.html', context)

def success(request):
    request.session.set_expiry(0)
    # Retrieve data from Orders model
    order_instance = Orders.objects.last()
    note = order_instance.note
    order_data = order_instance.order_data

    context = {
        'note': note,
        'order': order_data,
    }

    print(order_data)
    print(note)
    return render(request, 'success.html', context)
