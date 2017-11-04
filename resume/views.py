from django.shortcuts import render
from django.http import HttpResponse

from .models import Resume, Job, Tool

# Create your views here.
def home(request):
    return render(request, "resume/home.html")

def resume(request):
    resume = Resume.objects.all()[0]
    return render(request, "resume/resume.html", {"resume": resume})

def projects(request):
    return render(request, "resume/project_list.html")

def contact(request):
    return render(request, "resume/contact.html")
