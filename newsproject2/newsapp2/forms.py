from .models import madhan 
from django import forms
from django.contrib.auth.forms import UserCreationForm

class formsclass(forms.ModelForm):

    class Meta:
        model = madhan
        fields = "__all__"