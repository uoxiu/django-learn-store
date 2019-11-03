from django.shortcuts import render, redirect

from store.forms import ProductForm
from store.models import Product


def index(request):
    products = Product.objects.all()

    return render(request, 'home.html', {
        'products': products
    })


def product_add(request):
    return render(request, 'product_add.html', {
        'add_form': ProductForm()
    })


def product_add_save(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()

        return redirect('home')

    return render(request, 'product_add.html', {
        'add_form': form
    })


def product_view(request, pk):
    product = Product.objects.get(pk=pk)

    return render(request, 'product_view.html', {
        'product': product
    })
