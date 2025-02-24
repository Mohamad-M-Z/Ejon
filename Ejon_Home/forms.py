from django import forms
from .models import Contact, Product, Cart

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

class ProductForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = ['quantity']
