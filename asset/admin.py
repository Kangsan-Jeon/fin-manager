from django.contrib import admin

# Register your models here.
from .models import MyStock

admin.site.register(MyStock)
