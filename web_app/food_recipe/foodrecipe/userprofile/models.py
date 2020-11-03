from django.db import models
from main.models import User
# Create your models here.




class Profile(models.Model):
    people=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.CharField(max_length=200)
    description= models.CharField(max_length=200)
    # profile_pic=models.ImageField(upload_to='pics')
    
