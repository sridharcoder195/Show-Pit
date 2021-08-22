from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.
def home_page(request, c_slug=None):
    c_page = None
    product = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        product = Products.objects.filter(cat=c_page, available=True)
    else:
        product = Products.objects.all().filter(available=True)
    cat = Category.objects.all()
    paginator = Paginator(product, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)

    return render(request,'index.html', {'prod': product, "ct": cat, 'pg': pro})


def pd(request, c_slug, product_slug):
    try:
        prod = Products.objects.get(cat__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'pr': prod})


def search(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Products.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request, 'search.html', {'qr': query, 'search': prod})
