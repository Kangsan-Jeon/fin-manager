from django.urls import path

from . import views

app_name = "api"
urlpatterns = [
    # ex) /
    # path('', views.base, name="base"),

    # ex) /index
    path('', views.apiOverview, name="api-overview"),
    path('portfolio-list/', views.portfolioList, name='portfolio-list'),
]