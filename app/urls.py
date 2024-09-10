from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name= 'home'),
    path('register/', register, name= 'register'),
    path('login/', login_user, name= 'login_user'),
    path('logout/', logout_user, name= 'logout_user'),

]
