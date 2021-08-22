from django.shortcuts import render, redirect, get_object_or_404
from shop.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def cart_page(request, tot=0, count=0):
    global ct_items,a
    try:
        ct = cart.objects.get(cart_id=c_id(request))
        ct_items = catitems.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot+= (i.prodt.price * i.quan)
            count += i.quan
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci': ct_items, 't': tot, 'cn': count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_to_cart(request, prod_id):
    prod = Products.objects.get(id=prod_id)
    try:
        ct = cart.objects.get(cart_id=c_id(request))
    except cart.DoesNotExist:
        ct = cart.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_item = catitems.objects.get(prodt=prod, cart=ct)
        if c_item.quan < c_item.prodt.stock:
            c_item.quan += 1
        c_item.save()

    except catitems.DoesNotExist:
        c_item = catitems.objects.create(prodt=prod, quan=1, cart=ct)
        c_item.save()
    return redirect('cart')


def miin_cart(request, prod_id):
    ct = cart.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Products, id=prod_id)
    c_iems = catitems.objects.get(prodt=prod, cart=ct)
    if c_iems.quan > 1:
        c_iems.quan -= 1
        c_iems.save()

    else:
        c_iems.delete()

    return redirect('cart')


def delete(request,prod_id):
    ct = cart.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Products, id=prod_id)
    c_iems = catitems.objects.get(prodt=prod)
    c_iems.delete()
    return redirect('cart')
