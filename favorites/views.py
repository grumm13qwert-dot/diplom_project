from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Favorite

@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    Favorite.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user)

    return render(request, 'favorites/favorites.html', {
        'favorites': favorites
    })


@login_required
def remove_favorite(request, product_id):
    Favorite.objects.filter(
        user=request.user,
        product_id=product_id
    ).delete()

    return redirect(request.META.get('HTTP_REFERER', '/'))


