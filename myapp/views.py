from django.http import *
from django.shortcuts import render,redirect
from django.template import RequestContext
# from birthdayreminder.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from myapp.models import Phone

@login_required(login_url='/login/')
def main(request):
   phones = Phone.objects.all()
   res =''
   
   for elt in phones:
      if(request.user.id == elt.user_id):
         res += elt.first_name + elt.last_name + str(elt.phonenumber) + "\n"
   return render(request, "myapp/welcome.html", {'phones' : res})

def login_user(request):
   logout(request)
   username = password = ''
   if request.POST:
      username = request.POST['username']
      password = request.POST['password']
   user = authenticate(username=username, password=password)
   if user is not None:
      if user.is_active:
         login(request, user)
         return HttpResponseRedirect('/main/')
   return render(request,'myapp/login.html',{})

def addPhone(request):
   firstname=lastname=phone=""
   if request.POST:
      firstname = request.POST['firstname']
      lastname = request.POST['lastname']
      phone = request.POST['phone']

   newPhone = Phone(
      first_name = firstname, last_name = lastname, 
      phonenumber = phone , user_id = request.user.id
   )
   newPhone.save()
   return HttpResponseRedirect('/main/')
      
