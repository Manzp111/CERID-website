from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path("home/",views.base,name="base"),
    path("",views.home,name="home"),
    path("donate/",views.donate,name="donate"),
    path("leadership/",views.leaderTeam,name="leadership"),
    path("mission/",views.mission,name="mission"),
    path("cred/",views.cred,name='cred'),
    path("contact/",views.contact,name='contact'),
    path("transparency/",views.transparency,name='transparency'),
    # path('testemonials/video/',views.view_testmonials,name='viewTestimonials'),
    path('partners/',views.partner,name='partners'),
    path('document/',views.document,name='document'),
    path('our_project/', views.health_research_home, name='health_research_home'),
    path('our_project/projects/<slug:slug>/', views.project_detail, name='project_detail'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

