from django import forms
from django.db import models
from django.forms import ModelForm
from .models import ChatMessage
class ChatMessageForm(ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['body','pdf']
