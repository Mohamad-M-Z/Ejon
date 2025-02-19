from django.urls import path
from . import views
app_name = 'Cart'

urlpatterns = [

    path('cart/', views.view_cart , name='cart-view'),
    path('cart-add/<int:product_id>/', views.add_to_cart , name='add-cart'),
     path('cart-remove/<int:item_id>/', views.remove_cart , name='remove-cart'),

]