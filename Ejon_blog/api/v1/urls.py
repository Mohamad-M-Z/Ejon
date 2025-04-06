from django.urls import path, include
from . import views

app_name = 'api-v1'

urlpatterns = [
    path('api/v1/list/', views.Bloglist , name="blog-list"),
    path('api/v1/detail/<id>/', views.BlogDetail , name="blog-detail"),
]

