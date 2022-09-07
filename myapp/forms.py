from django import forms
from django.contrib.auth.models import User
from myapp.models import Phone  
  

class ContactForm(forms.ModelForm):  
    class Meta:  
        model = Phone  
        fields = ['first_name', 'last_name', 'phonenumber'] 
    
    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     if self.instance.user:
    #         self.fields['user'].queryset = User.objects.filter( user = self.instance.user )