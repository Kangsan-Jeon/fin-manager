from django.urls import path

from . import views

app_name = "api"
urlpatterns = [
    # ex) /
    # path('', views.base, name="base"),

    # ex) /index
    path('', views.apiOverview, name="api-overview"),
    path('portfolio-list/', views.portfolioList, name='portfolio-list'),
    path('portfolio-detail/<str:pk>/', views.portfolioDetail, name='portfolio-detail'),
    path('portfolio-create/', views.portfolioCreate, name='portfokio-create'),
    path('portfolio-update/<str:pk>/', views.portfolioUpdate, name='portfokio-update'),
    path('portfolio-delete/<str:pk>/', views.portfolioDelete, name='portfokio-delete'),

]