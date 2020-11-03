
from django.urls import path
from . import  views
urlpatterns = [
     path('profile/',views.User_Profile,name ='profile'),    
   
]