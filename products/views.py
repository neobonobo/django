from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Product, ProductImage
from django.contrib import messages
from .forms import ProductForm, ProductImageForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid() :
            # Save the product first
            product = product_form.save()

            # Handle multiple image uploads
            images = request.FILES.getlist('image')
            for image in images:
                ProductImage.objects.create(product=product, image=image)

            return redirect('product_list')  # or any other page

    else:
        product_form = ProductForm()

    return render(request, 'create_product.html', {'product_form': product_form})
