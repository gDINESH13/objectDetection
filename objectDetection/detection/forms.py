from django import forms

class NameForm(forms.Form):
    docFile=forms.FileField(label="RawImage")