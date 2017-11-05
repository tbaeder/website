from django.shortcuts import render
from django.http import HttpResponse

from .models import Resume, Job, Tool

# Create your views here.

def resume(request, id):
    if not id:
        id=1
    resumes = Resume.objects.filter(id=id)
    if not resumes.count():
        resumes = Resume.objects.filter(id=1)
    resume = resumes[0]
    return render(request, "resume/resume.html", {"resume": resume})

def projects(request):
    return render(request, "resume/project_list.html")

def contact(request):
    return render(request, "resume/contact.html")

def home(request):
    return render(request, "resume/home.html")
