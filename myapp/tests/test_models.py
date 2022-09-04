from django.test import TestCase
from myapp.models import Phone 


class PhoneTestCase(TestCase):
    def setUp(self):
        Phone.objects.create(
             first_name = "alireza", last_name = "najmipour", 
             phonenumber = "0913" , user_id = 1
        )
        Phone.objects.create(
             first_name = "arshia", last_name = "najmipour", 
             phonenumber = "0937" , user_id = 1
        )