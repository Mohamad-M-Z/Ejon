from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list', views.BlogViewSet, basename='blog')
router.register('category', views.CategoryModelViewSet, basename='category')

app_name = 'api-v1'

urlpatterns = router.urls




