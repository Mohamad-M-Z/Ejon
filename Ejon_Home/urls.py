from django.contrib import admin
from django.urls import path
from . import views


app_name = "Ejon"

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('about/', views.about.as_view(), name='about'),
    path('shop/', views.ListView.as_view(), name='shop'),
    path('services/', views.services.as_view(), name='services'),
    path('contact/', views.contactView.as_view(), name='contact'),
    path('detail/<int:pk>/', views.detail_view.as_view(), name='detail'),
   


]