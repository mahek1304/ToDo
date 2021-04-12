from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):    #form creation for Task model
    
    title = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Add New Task'}))
    
    class Meta:                     #we need to give minimal 2 values:
        
        model = Task                #one would be the name of the model for which we are creating form
        fields = '__all__'          #and which fields are we allowing in that form (all the fields are allowed)
