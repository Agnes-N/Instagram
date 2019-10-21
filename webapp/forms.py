from django import forms
from .models import Profile,Image,Comments

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'date', 'firstname', 'lastname']
        # widgets = {
        #     'profile': forms.CheckboxSelectMultiple(),
        # }

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_name', 'profile_pic','date','user', 'profile', 'likes']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

class commentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['commented_image', 'posted_by','profile']
        # widgets = {
        #     'profile': forms.CheckboxSelectMultiple(),
        # }