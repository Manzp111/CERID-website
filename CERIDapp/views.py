from django.shortcuts import render
from . import  models
from .models import ImageSlider


def base(request):
    return render(request, 'base.html')

def home(request):
    sliders = ImageSlider.objects.all()
    return render(request, 'homepages/home.html', {'slides': sliders})


def donate(request):
    return render(request,'homepages/donate.html')


def leaderTeam(request):
    return render(request,'aboutusPage/leadership.html')


def mission(request):
    return render(request,'aboutusPage/mission.html')


def cred(request):
    return render(request,'homepages/cred.html')


def contact(request):
    return render(request,'homepages/contact.html')





