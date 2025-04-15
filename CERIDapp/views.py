from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def home(request):
    return  render(request,'homepages/home.html')


def donate(request):
    return render(request,'homepages/donate.html')


def leaderTeam(request):
    return render(request,'aboutusPage/leadership.html')


def mission(request):
    return render(request,'aboutusPage/mission.html')



