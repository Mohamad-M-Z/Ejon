from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, View
from .models import Product, Cart
from .forms import ContactForm, ProductForm
from django.views.generic.edit import FormView
from django.views.generic.edit import FormMixin
from django.urls import reverse

# Create your views here.



class Home(ListView):
    model = Product
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



class detail_view(FormMixin, DetailView):
    template_name = 'Ejon_home/detail_shop.html'
    model = Product
    form_class = ProductForm
    context_object_name = "product"


    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(detail_view, self).get_context_data(**kwargs)
        context['form'] = ProductForm(initial={'count': self.object})
        return context

    def form(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(detail_view, self).form_valid(form)


 
