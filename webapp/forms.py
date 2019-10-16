class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'date']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }