from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from favorites.models import Favorite

from reviews.models import Review

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:8]  # последние 8 товаров

    return render(request, 'home.html', {
        'categories': categories,
        'products': products
    })




def product_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category_id:
        products = products.filter(category_id=category_id)

    categories = Category.objects.all()

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_id,
        'query': query
    })



def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    reviews = Review.objects.filter(product=product).order_by('-created_at')
    is_favorite = False

    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(
            user=request.user,
            product=product
        ).exists()
    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'is_favorite': is_favorite
    })
