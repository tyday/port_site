# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.TextInput(
        attrs={'class' : 'email-from',
        'placeholder':'your email'}),
        required=True)
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class' : 'email-subject',
                'placeholder':'Subject'}), 
        required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'id' : 'email-message'}), required=True)
    