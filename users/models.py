from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class User(AbstractUser):
    user_id = models.CharField("ID of User", blank=True, max_length=255)
    name = models.CharField("Name of User", blank=True, max_length=255)
    
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"user_id": self.user_id})
