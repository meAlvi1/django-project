from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Order


def say_hello(request):
    queryset = Order.objects.filter(customer__id=1)

    return render(request, 'hello.html', {'name': 'Alvi', 'products': list(queryset)})
