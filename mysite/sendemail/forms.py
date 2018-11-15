# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    from_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Name*'}),
        required=True)
    from_email = forms.EmailField(widget=forms.TextInput(
        attrs={'class' : 'email-from',
        'placeholder':'Email*'}),
        required=True)
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class' : 'email-subject',
                'placeholder':'Subject'}),
        required=False)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder':'Message'}),
        required=False)
    