from django import forms
from .models import Profile,Image

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'date', 'firstname', 'lastname']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_name', 'profile_pic','date','user']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }