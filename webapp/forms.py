from django import forms
from .models import Image

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_name', 'date']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }