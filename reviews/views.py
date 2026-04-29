from django.shortcuts import redirect
from .models import Review
from products.models import Product


def add_review(request, product_id):
    if request.method == 'POST' and request.user.is_authenticated:
        text = request.POST.get('text')
        product = Product.objects.get(id=product_id)

        Review.objects.create(
            user=request.user,
            product=product,
            text=text
        )

    return redirect('product_detail', id=product_id)