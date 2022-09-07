from django.http import *
import re
from django.shortcuts import render,redirect
from django.template import RequestContext
# from birthdayreminder.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from myapp.models import Phone
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.core.validators import RegexValidator
from myapp.forms import ContactForm
from django.views.generic.edit import UpdateView,CreateView
from django.contrib.auth import logout


class signup(View):
   def post(self,request):
      form = UserCreationForm(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password1')
         user = authenticate(username=username, password=raw_password)
         login(request, user)
         return HttpResponseRedirect('/main/')
      return render(request,'myapp/login.html',{})

   def get(self,request):
      form = UserCreationForm()  
      context = {  
        'form':form  
      }      
      return render(request, "myapp/signup.html",context)
  



class main(View):
   def get(self,request):
      
      if request.user.is_authenticated:
         phones = Phone.objects.all()
         res =[]
         for elt in phones:

            if(request.user.id == elt.user_id):
               res.append(elt)

         return render(request, "myapp/welcome.html", {'phones' : res})

      else:
         
         return render(request,'myapp/login.html',{"msg":"please login first!"})



class login_user(View):
   def post(self,request):
      logout(request)
      username = password = ''
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
         if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/main/')
      return render(request,'myapp/login.html',{"msg":"wrong username or password!"})
   def get(self,request):
      logout(request)
      return render(request,'myapp/login.html',{"msg":""})


class deletePhone(View):
   def get(self, request,phone_id):
      Phone.objects.filter(id=phone_id).delete()
      return HttpResponseRedirect('/main/')


class EditPhone(UpdateView):
   model = Phone
   form_class = ContactForm
   template_name = 'myapp/phoneForm.html'
   success_url = '/main'


class CreatePhone(CreateView):
   model = Phone
   form_class = ContactForm
   template_name = 'myapp/phoneForm.html'
   success_url = '/main'

   def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
