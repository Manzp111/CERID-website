from django.shortcuts import render, redirect
from . import  models
from .models import ImageSlider, VisionItem,HeroSection, Project
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import MessageForm
from django.core.mail import send_mail

from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse



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
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message_instance = form.save()

            
            subject = "Thank you for contacting us!"
            message_body = f"""
            Dear {message_instance.first_name},

            Thank you for reaching out to us. We have received your message and will get back to you soon!

            Here is a copy of your message:
            ----------------------------------------
            {message_instance.message}
            ----------------------------------------

            Best regards,
            CERID Team
            """

            from_email = 'gilbertnshimyimana11@gmail.com'  
            recipient_list = [message_instance.email]  

            send_mail(subject, message_body, from_email, recipient_list, fail_silently=False)

            return redirect('home')
    else:
        form = MessageForm()
    return render(request, 'homepages/contact.html', {'form': form})



def transparency(request):
    return render(request,'homepages/transparency.html')


#def view_testmonials(request):
    # testimonials = models.Testimonial.objects.all()
   # return render(request, 'otherLinks/transparency.html')

def transparency(request):
    # Fetching data from the models
    FinancialReport = models.FinancialReport.objects.all()
    ImpactMetric = models.ImpactMetric.objects.all()
    TeamMember = models.TeamMember.objects.all()
    LegalDocument = models.LegalDocument.objects.all()

    context = {
        'financial_reports': FinancialReport,
        'impact_metrics': ImpactMetric,
        'team': TeamMember,
        'legal_docs': LegalDocument,
    }
    return render(request, 'trancy/transparency.html', context)

def  partner(request):
    return render(request, 'aboutusPage/paterners.html')

def document(request):
    return render(request, 'aboutusPage/documents.html')



def health_research_home(request):

    hero =HeroSection.objects.filter(is_active=True).first()
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