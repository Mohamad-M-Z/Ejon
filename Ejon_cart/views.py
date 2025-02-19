from django.shortcuts import render, redirect, reverse
from Ejon_Home.models import Cart, Product


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


def remove_cart(request, item_id):
    product = Product.objects.get(pk=item_id)
    cart = Cart.objects.get(product=product, user=request.user)
    cart.quantity -= 1
    cart.delete()
    return redirect('/')
