from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

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

def plan(request, user_id):
    return HttpResponse("Here is yout budget plan")

def portfolio(request, stock_ticker):
    my_stock = get_object_or_404(MyStock, pk=stock_ticker)
    return render(request, 'finance/portfolio.html', {"my_stock": my_stock})

def record(request, user_id):
    return HttpResponse("I record your details of exchange, dividend and long/short")

def logout_view(request):
    logout(request)
    return render(request, 'finance/base.html')

