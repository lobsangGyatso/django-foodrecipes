from django.shortcuts import render

from .models import Profile
from .forms import ProfileForm

# Create your views here.


def User_Profile(request):
    user_obj=request.user
    return render(request,'profile.html',{'userinfo':user_obj})

