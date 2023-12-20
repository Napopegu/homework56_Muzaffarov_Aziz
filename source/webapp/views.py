from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product, Category


def products_view(request):
    products = Product.objects.all()
    return render(request, template_name='products_list.html', context={'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, template_name='product_view.html', context={'product': product})


def product_add_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, template_name='product_create.html', context={'categories': categories})
    elif request.method == "POST":
        product = Product.objects.create(
            title=request.POST.get('title'),
            price=request.POST.get('price'),
            image=request.POST.get('image'),
            description=request.POST.get('description'),
            category_id=request.POST.get('category_id')
        )
        return redirect("product_view", pk=product.pk)


def category_add_view(request):
    if request.method == "GET":
        return render(request, template_name='category_create.html')
    elif request.method == "POST":
        Category.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),

        )
        return redirect("index")
