from django.shortcuts import render, HttpResponse, redirect

def index(req):
    return render(req, 'blogs/index.html')

def buy(req):

    if req.method == "POST":
        quantity = req.POST['quantity']
        product_id = req.POST['product_id']
        if product_id == '1000':
            price = int(quantity) * 19.99
        if product_id == '2000':
            price = int(quantity) * 29.99
        if product_id == '3000':
            price = int(quantity) * 4.99
        if product_id == '4000':
            price = int(quantity) * 49.99
        try:
            req.session['total'] += price
        except KeyError:
            req.session['total'] = price
        try:
            req.session['count'] += int(quantity)
        except KeyError:
            req.session['count'] = int(quantity)
        req.session['price'] = price
        return redirect('/amadon/cart')
    else:
        return redirect('/')

def cart(req):
    return render(req, 'blogs/cart.html')
def clear(req):
    req.session.clear()
    return redirect('/')
