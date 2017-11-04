from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "resume/home.html")

def resume(request):
    return render(request, "resume/resume.html")

def projects(request):
    return render(request, "resume/project_list.html")

def contact(request):
    return render(request, "resume/contact.html")
