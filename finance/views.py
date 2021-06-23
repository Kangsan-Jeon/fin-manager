from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse

from .models import MyStock

from django.contrib.auth import logout


# Create your views here.

def base(request):
    return render(request, 'finance/base.html')

def index(request):
    my_stocks = MyStock.objects.all()
    context = {
        'my_stocks': my_stocks
    }
    return render(request, 'finance/index.html', context)

def budget(request):
    return render(request, 'finance/budget.html')

def portfolio(request):
    my_stocks = MyStock.objects.all()
    context = {
        'active_page': 'portfolio',
        'my_stocks': my_stocks
    }
    return render(request, 'finance/portfolio.html', context)

def record(request, user_id):
    return HttpResponse("I record your details of exchange, dividend and long/short")
