from django import forms
from .models import Contact, Product

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['count', 'size']
