from django.urls import path, include
from . import views


urlpatterns = [
     path('blog/', views.BlogView.as_view(), name="blog"),
     path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='detail-blog'),
     path('blog/', include('Ejon_blog.api.v1.urls') ),
]