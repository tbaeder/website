"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from resume.views import *
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contactme/$', contact, name="contact"),
    url(r'^projects/$', projects, name="projects"),
    url(r'^home/$', home, name="home"),
    url(r'^resumes/(?P<id>\d*)$', resume, name="resume"),
    url(r'^resumes/$', resume, name="resume"),
    url(r'^messages/$', MessageListView.as_view(), name="messages"),
    url(r'^messages/delete/$', delete_message, name="delete_message"),
    url(r'^$', RedirectView.as_view(url='/home/'))
]
