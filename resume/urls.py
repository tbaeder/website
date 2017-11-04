from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^projects/$', views.projects, name="projects"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^resume/$', views.contact, name="resume"),
]
