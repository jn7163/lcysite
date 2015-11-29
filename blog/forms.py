from django import forms
from django.db import models
from django.utils import timezone
#from django.forms import TextInput,Textarea

class NewReplyForm(forms.Form):
    name=forms.TextInput()
    body=forms.Textarea()
    passage=forms.TextInput()
    
