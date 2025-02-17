from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Product
from .forms import ContactForm
from django.views.generic.edit import FormView

# Create your views here.


class Home(TemplateView):
    template_name = 'Ejon_home/home.html'


class about(TemplateView):
    template_name = 'Ejon_home/about.html'


class services(TemplateView):
    template_name = 'Ejon_home/services.html'


class ListView(ListView):
    model = Product
    template_name = "Ejon_home/shop.html"


class contactView(FormView):
    template_name = 'Ejon_home/contact.html'
    form_class = ContactForm
    success_url = "/contact/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class detail_view(TemplateView):
    template_name = 'Ejon_home/detail_shop.html'


