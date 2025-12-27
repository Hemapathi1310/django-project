from django.shortcuts import render, redirect

def cart_view(request):
    cart = request.session.get('cart', [])
    total = sum(item['price'] for item in cart)
    count = len(cart)

    return render(request, 'cart/index.html', {
        'cart': cart,
        'total': total,
        'count': count
    })


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')

        if name and price:
            cart = request.session.get('cart', [])
            cart.append({
                'name': name,
                'price': float(price)
            })
            request.session['cart'] = cart
            request.session.modified = True

    return redirect('cart-view')


def delete_item(request, index):
    cart = request.session.get('cart', [])
    if 0 <= index < len(cart):
        cart.pop(index)
    request.session['cart'] = cart
    return redirect('cart-view')


def clear_cart(request):
    request.session['cart'] = []
    return redirect('cart-view')
