from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path("",views.base,name="base"),
    path("home/",views.home,name="home"),
    path("donate/",views.donate,name="donate"),
    path("leadership/",views.leaderTeam,name="leadership"),
    path("mission/",views.mission,name="mission"),

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

