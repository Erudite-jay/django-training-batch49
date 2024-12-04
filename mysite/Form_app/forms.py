from django import forms
from .models import FileFormUpload
# class FileForm(forms.Form):
#     name=forms.CharField(max_length=256)
#     file=forms.FileField()

class FileForm(forms.ModelForm):
    class Meta:
        model=FileFormUpload
        fields=['name','file']