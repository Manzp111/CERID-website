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
    path("our_project/",views.our_project, name="our_project"),

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

