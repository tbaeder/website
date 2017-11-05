from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .models import Resume,Message
from .forms import ContactMeForm

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
    if request.method == "POST":
        form = ContactMeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "resume/contact.html", {"contact_me_form": form, "thanks": True})
    else:
        form = ContactMeForm()
    return render(request, "resume/contact.html", {"contact_me_form": form})

def home(request):
    return render(request, "resume/home.html")

class MessageListView(generic.ListView):
    model = Message

@csrf_exempt
def delete_message(request):
    id = request.POST["message_id"]
    if not id:
        return JsonResponse({"success": False})
    message = Message.objects.filter(id=id)
    if not message.count():
        return JsonResponse({"success": False})
    message[0].delete()
    return JsonResponse({"success": True, "data-id": id })
