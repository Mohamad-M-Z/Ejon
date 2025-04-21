from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
     path('blog/', views.BlogView.as_view(), name="blog"),
     path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='detail-blog'),
     path('blog/api/v1/', include('Ejon_blog.api.v1.urls') ),
]