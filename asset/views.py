from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse

from .models import MyStock

from django.contrib.auth import logout


# Create your views here.

def base(request):
    return render(request, 'asset/base.html')

def index(request):
    my_stocks = MyStock.objects.all()
    context = {
        'my_stocks': my_stocks
    }
    return render(request, 'asset/index.html', context)

def budget(request):
    return render(request, 'asset/budget.html')

def portfolio(request):
    my_stocks = MyStock.objects.all()
    context = {
        'active_page': 'portfolio',
        'my_stocks': my_stocks
    }
    return render(request, 'asset/portfolio.html', context)

def portfolio_usa(request):
    usa_stocks = MyStock.objects.filter(account="KW").order_by("ticker")
    context = {
        'active_page': 'portfolio-usa',
        'usa_stocks': usa_stocks
    }
    return render(request, 'asset/portfolio-usa.html', context)

def portfolio_kor(request):
    my_stocks = MyStock.objects.all()
    context = {
        'active_page': 'portfolio-kor',
        'my_stocks': my_stocks
    }
    return render(request, 'asset/portfolio-korea.html', context)

def portfolio_iruda(request):
    my_stocks = MyStock.objects.all()
    context = {
        'active_page': 'portfolio-iruda',
        'my_stocks': my_stocks
    }
    return render(request, 'asset/portfolio-iruda.html', context)

def portfolio_etc(request):
    my_stocks = MyStock.objects.all()
    context = {
        'active_page': 'portfolio-etc',
        'my_stocks': my_stocks
    }
    return render(request, 'asset/portfolio-etc.html', context)

def record(request, user_id):
    return HttpResponse("I record your details of exchange, dividend and long/short")
