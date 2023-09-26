from django import forms
from django.contrib.auth.models import User
from django import forms
from uploads.models import *

class UploadItemForm(forms.ModelForm):
    class Meta:
        model=UploadItem
        fields= '__all__'
        exclude=['uploaded_by']
