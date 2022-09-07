from django.test import TestCase
from myapp.models import Phone 
from django.contrib.auth import get_user_model
from django.test import TransactionTestCase, Client
from myapp.models import Phone
from myapp.forms import ContactForm
from django.contrib.auth.models import User
from urllib.parse import urlencode


class PhoneTestCase(TestCase):
    def setUp(self):
        self.form = ContactForm
        self.user = User.objects.create(username = "test1" )
        self.user.set_password ("test")
        self.user.save()
        self.contacts = Phone
        self.client = Client()
        

    def test_update_contact(self):
        data = { "last_name" : "najmipour", "first_name" : "arshia" ,
                  "phonenumber" : "09131296702" ,"user" :self.user.id }
        
                            
        form = self.form( data )
        form.save()
        contact = self.contacts.objects.first()
        self.client.login(username=self.user.username, password='test')
        edited_data = { "last_name" : "najmipour", "first_name" : "arshia" ,
                        "phonenumber" : "09131234567" ,"user" :self.user.id }

        response=self.client.put( '/edit/phone/'+ str(contact.id) , urlencode(edited_data) , True )

        self.assertEqual( contact.phonenumber , "09131234567" )


    def test_contact_form_correct_data (self):

        data = { "last_name" : "najmipour", "first_name" : "arshia" ,
                  "phonenumber" : "09131296702" ,"user" :self.user.id}
                            
        form = self.form( data )
        form.save()
        

    def test_contact_form_wrong_data (self):

        data = { "last_name" : "najmipour", "first_name" : "arshia" ,
                  "phonenumber" : "091312" ,"user" :self.user.id}
                            
        form = self.form( data )
        form.save()




    def test_get_login(self):
        response=self.client.get('/login', {}, True)
        self.assertEqual(response.status_code, 200)  


    def test_get_main_without_login(self):
        response=self.client.get('/main', {}, True)
        self.assertEqual(response.status_code, 404)   


    def test_get_main_with_login(self):
        self.client.login(username=self.user.username, password='test')
        response = self.client.get('/main', {}, True)
        self.assertEqual(response.status_code, 200)    


    def test_delete_contact(self):
        data = { "last_name" : "najmipour", "first_name" : "arshia" ,
                  "phonenumber" : "091312967222" ,"user" :self.user.id }
                            
        form = self.form( data )
        form.save()
        contact = self.contacts.objects.first()
        self.client.login(username=self.user.username, password='test')
        response=self.client.get('/delete/phone/'+str(self.contacts.objects.first().id), {}, True)

        self.assertEqual(response.status_code, 200)    
        self.assertEqual(self.contacts.objects.count(), 0 )   
    

