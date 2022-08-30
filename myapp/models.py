
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Phone(models.Model):
    first_name = models.CharField(max_length=42)
    last_name = models.CharField(max_length=42)
    phonenumber = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
