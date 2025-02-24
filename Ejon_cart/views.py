from django.shortcuts import render, redirect, reverse, get_object_or_404
from Ejon_Home.models import Cart, Product
from django.views.generic import DeleteView, CreateView
# Create your views here.


def view_cart(request):
    cart_items = Cart.objects.all()
    context = {'cart_items':cart_items}
    return render(request, 'Ejon_home/cart.html', context)




  
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart,created  = Cart.objects.get_or_create(product=product, user=request.user)
    cart.quantity += 1
    cart.save()
    return  redirect('Cart:cart-view')


# class CartCreateView(CreateView):
#     model = Cart
#     fields = ['quantity',  'id']
#     success_url = '/'





class CartDeleteView(DeleteView):
    model = Cart
    success_url = '/cart/'

