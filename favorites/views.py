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
def remove_favorite(request, favorite_id):
    fav = get_object_or_404(Favorite, id=favorite_id, user=request.user)
    fav.delete()
    return redirect('favorites_list')


@login_required
def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('product')

    sort = request.GET.get('sort')

    if sort == 'price_asc':
        favorites = favorites.order_by('product__price')
    elif sort == 'price_desc':
        favorites = favorites.order_by('-product__price')
    elif sort == 'name':
        favorites = favorites.order_by('product__name')
    elif sort == 'new':
        favorites = favorites.order_by('-id')

    return render(request, 'favorites/favorites.html', {
        'favorites': favorites,
        'sort': sort
    })