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
        'Create': '/portfolio-create/',
        'Update': '/portfolio-update/<str:pk>/',
        'Delete': '/portfolio-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def portfolioList(request):
    portfolios = Portfolio.objects.all()
    serializer = PortfolioSerializer(portfolios, many=True)
    return Response(serializer.data)
