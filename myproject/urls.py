"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import main,login_user,EditPhone,deletePhone,signup,CreatePhone
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("admin/", admin.site.urls),
    path('main/', login_required(main.as_view())),
    path('login/', login_user.as_view()),
    path('signup',signup.as_view()),
    path('delete/phone/<phone_id>',login_required(deletePhone.as_view())),
    path('addPhone',login_required(CreatePhone.as_view())),
    path('edit/phone/<int:pk>',login_required(EditPhone.as_view()) ,name='contact_edit'),
]
