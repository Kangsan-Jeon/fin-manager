from django.urls import path

from . import views

app_name = "finance"
urlpatterns = [
    # ex) /
    # path('', views.base, name="base"),

    # ex) /index
    path('', views.index, name="index"),

    # ex) /daisyjeon/plan
    path('budget/', views.budget, name="budget"),
    
    # ex) /daisyjeon/portfolio
    path('portfolio/<str:stock_ticker>/', views.portfolio, name="portfolio"),

    # ex) /daisyjeon/record
    path('record/', views.record, name="record"),

]