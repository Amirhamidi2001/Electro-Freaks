from django import forms
from website.models import Contact, Newsletter


class ContactForm(forms.ModelForm):
    """
    The ContactForm model is used for processing a contact form. It is a ModelForm that is based on the Contact model
    """

    class Meta:
        model = Contact
        fields = "__all__"


class NewsletterForm(forms.ModelForm):
    """
    The NewsletterForm model is used for processing a newsletter subscription form
    """

    class Meta:
        model = Newsletter
        fields = "__all__"
