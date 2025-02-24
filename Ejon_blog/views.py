from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog
# Create your views here.

class BlogView(ListView):
    model = Blog
    paginate_by = 6
    template_name = 'Ejon_blog/blog.html'



class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'


