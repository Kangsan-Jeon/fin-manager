from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PortfolioSerializer
from asset.models import Portfolio

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Portfolio List': '/portfolio-list/',
        'Portfolio Detail': '/portfolio-detail/<str:pk>/',
        'Portfolio Create': '/portfolio-create/',
        'Portfolio Update': '/portfolio-update/<str:pk>/',
        'Portfolio Delete': '/portfolio-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def portfolioList(request):
    portfolios = Portfolio.objects.all()
    serializer = PortfolioSerializer(portfolios, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def portfolioDetail(request, pk):
    portfolio = Portfolio.objects.get(ticker=pk)
    serializer = PortfolioSerializer(portfolio, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def portfolioCreate(request):
    serializer = PortfolioSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def portfolioUpdate(request, pk):
    portfolio = Portfolio.objects.get(ticker=pk)
    serializer = PortfolioSerializer(instance=portfolio, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def portfolioDelete(request, pk):
    portfolio = Portfolio.objects.get(ticker=pk)
    portfolio.delete()
    return Response("Portfolio succesfully delete!")