from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove/<int:product_id>/', views.remove_favorite, name='remove_favorite'),
    path('', views.favorites_list, name='favorites_list'),
]