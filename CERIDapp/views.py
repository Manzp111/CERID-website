from django.shortcuts import render
from . import  models
from .models import *



def base(request):
    return render(request, 'base.html')

def home(request):
    sliders = ImageSlider.objects.all()
    return render(request, 'homepages/home.html', {'slides': sliders})


def donate(request):
    return render(request,'homepages/donate1.html')


def leaderTeam(request):
    return render(request,'aboutusPage/leadership.html')


def mission(request):
    return render(request,'aboutusPage/mission.html')


def cred(request):
    return render(request,'homepages/cred.html')


def contact(request):
    return render(request,'homepages/contact.html')


def transparency(request):
    return render(request,'homepages/transparency.html')


#def view_testmonials(request):
    # testimonials = models.Testimonial.objects.all()
   # return render(request, 'otherLinks/transparency.html')

def transparency(request):
    context = {
        'financial_reports': FinancialReport.objects.all(),
        'impact_metrics': ImpactMetric.objects.all(),
        'team': TeamMember.objects.all(),
        'legal_docs': LegalDocument.objects.all(),
    }
    return render(request, 'trancy/transparency.html', context)

def  partner(request):
    return render(request, 'aboutusPage/paterners.html')

def document(request):
    return render(request, 'aboutusPage/documents.html')



def health_research_home(request):
    hero = HeroSection.objects.filter(is_active=True).first()
    vision_items = VisionItem.objects.all()
    ongoing_projects = Project.objects.filter(status='ongoing')
    completed_projects = Project.objects.filter(status='completed')
    
    context = {
        'hero': hero,
        'vision_items': vision_items,
        'ongoing_projects': ongoing_projects,
        'completed_projects': completed_projects,
    }
    return render(request, 'our_project/index.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'our_project/index.html', {'project': project})