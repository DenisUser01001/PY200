from django import forms


class TemplateForm(forms.Form):
    contact_name = forms.CharField()
    contact_email = forms.EmailField()
    contact_message = forms.CharField(widget=forms.Textarea)
