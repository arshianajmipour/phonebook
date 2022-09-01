from django.http import *
from django.shortcuts import render,redirect
from django.template import RequestContext
# from birthdayreminder.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from myapp.models import Phone
from django.views.decorators.csrf import csrf_protect

@login_required(login_url='/login/')
def main(request):
   phones = Phone.objects.all()
   res =[]
   
   for elt in phones:
      if(request.user.id == elt.user_id):
         res.append(elt)
   return render(request, "myapp/welcome.html", {'phones' : res})

@csrf_protect
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

def deletePhone(request,phone_id):
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

