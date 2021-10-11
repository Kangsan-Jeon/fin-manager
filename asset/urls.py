from django.urls import path

from . import views

app_name = "asset"
urlpatterns = [
    # ex) /
    # path('', views.base, name="base"),

    # ex) /index
    path('', views.index, name="index"),

    # ex) /daisyjeon/plan
    path('budget/', views.budget, name="budget"),
    
    # ex) /daisyjeon/portfolio
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio/usa', views.portfolio_usa, name="portfolio-usa"),
    path('portfolio/kor', views.portfolio_kor, name="portfolio-kor"),
    path('portfolio/iruda', views.portfolio_iruda, name="portfolio-iruda"),
    path('portfolio/etc', views.portfolio_etc, name="portfolio-etc"),

    # ex) /daisyjeon/record
    path('record/', views.record, name="record"),

]