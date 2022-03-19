from django.shortcuts import redirect
from django.conf import settings
from django.views.generic import View, ListView
from base.models import Item
from collections import OrderedDict


class CartListView(ListView):
    model = Item
    template_name = 'pages/cart.html'
    
    
class AddCartView(View):
    def post(self, request):
        item_pk = request.POST.get('item_pk')
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', None)
        if cart is None or len(cart) == 0:
            items = OrderedDict()
            cart = {'items': items}
        if item_pk in cart['items']:
            cart['items'][item_pk] += quantity
        else:
            cart['items'][item_pk] = quantity
        request.session['cart'] = cart
        return redirect('/cart/')