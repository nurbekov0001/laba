from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.models import Product, CATEGORY_CHOICES
from webapp.forms import ProductForm, ProductDeleteForm


def index_view(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={'products': products})


def product_view(request, pk):
    products = get_object_or_404(Product, id=pk)
    return render(request, 'products_view.html', context={'products': products})


def product_create_view(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'products_create.html', {'category': CATEGORY_CHOICES})
    elif request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data.get("name"),
                description=form.cleaned_data.get("description"),
                category=form.cleaned_data.get("category"),
                remainder=form.cleaned_data.get("remainder"),
                price=form.cleaned_data.get("price")
            )

            return redirect('product_view', pk=product.id)
        return render(request, 'product_create.html', context={'form': form})


def product_update_view(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == 'GET':

        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'remainder': product.category,
            'price': product.category
        })
        return render(request, 'product_update.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data.get("name")
            product.description = form.cleaned_data.get("description")
            product.category = form.cleaned_data.get("category")
            product.remainder = form.cleaned_data.get("remainder")
            product.price = form.cleaned_data.get("price")
            product.save()
            return redirect('product_view', pk=product.id)
        return render(request, 'product_update.html', context={'form': form, 'product': product})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == 'GET':
        form = ProductDeleteForm()
        return render(request, 'product_delete.html', context={'product': product, 'form': form})
    elif request.method == 'POST':
        form = ProductDeleteForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['name'] != product.name:
                form.errors['name'] = ['Названия статей не совпадают']
                return render(request, 'product_delete.html', context={'product': product, 'form': form})
            product.delete()
            return redirect('product_list')
        return render(request, 'product_delete.html', context={'product': product, 'form': form})
