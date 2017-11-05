from django.forms import ModelForm,Textarea,TextInput

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Message

class ContactMeForm(ModelForm):

    class Meta:
        model = Message
        fields = ["title", "email", "message"]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'message': Textarea(attrs={'class': 'form-control', 'rows': '5'}),
        }
