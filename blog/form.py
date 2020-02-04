from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="",required=True)
    firstname = forms.CharField(label="",required=True)
    from_email = forms.EmailField(label="",required=True)
    message = forms.CharField(label="",widget=forms.Textarea, required=True)