
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import RegexValidator
import re

# Create your models here.
class Phone(models.Model):
    first_name = models.CharField(max_length=42,verbose_name = "first name")
    last_name = models.CharField(max_length=42,verbose_name = "last name")
    phonenumber = models.CharField(
        max_length = 20,
        verbose_name = "phone number",
        validators=[
            RegexValidator(
                regex=r"(0|\+98)?([ ]|-|[()]){0,2}9[1|2|3|4|5|6|7|8|9]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}",
                code='invalid phone number!',
            ),
        ]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE ,verbose_name = "user id")



