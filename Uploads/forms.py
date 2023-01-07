from django import forms

from .models import File


class DocumentForm(forms.ModelForm):
    class Meta:
        model = File # model is document
        fields = ('Title', 'File', )