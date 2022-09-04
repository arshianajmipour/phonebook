from django.http import *
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
      return render(request,'myapp/login.html',{"msg":""})

class addPhone(View):
   def post(self , request):
      firstname=lastname=phone=""
      
      firstname = request.POST['firstname']
      lastname = request.POST['lastname']
      phone = request.POST['phone']

      validate_phone = RegexValidator(r'/^(?:98|\+98|0098|0)?9[0-9]{9}$/', 'invalid phone number')

      try:
         validate_phone(phone)
         newPhone = Phone(
            first_name = firstname, last_name = lastname, 
            phonenumber = phone , user_id = request.user.id
         )
         newPhone.save()
      except:
         messages.success(request, ('invalid phone number'))
         HttpResponseRedirect('/main/',{"msg" : "invalid phone number!"})
      
      return HttpResponseRedirect('/main/')

class deletePhone(View):
   def get(self, request,phone_id):
      Phone.objects.filter(id=phone_id).delete()
      return HttpResponseRedirect('/main/')

def editPhone(request,phone_id):
   obj = Phone.objects.get(id=phone_id)
   if True:
       jsonData = json.loads(request.body)
       fn = jsonData.get('fn')
       ln = jsonData.get('ln')
       pn = jsonData.get('pn')
       obj = Phone(
         first_name = fn, last_name = ln, 
         phonenumber = pn , user_id = request.user.id
       )  
       obj.save()
   return HttpResponseRedirect('/main/')

