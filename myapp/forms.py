from django import forms

from myapp.models import Phone  
  
class ContactForm(forms.ModelForm):  
    class Meta:  
        model = Phone  
        fields = "__all__"  