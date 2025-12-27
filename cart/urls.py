from django.urls import path
from .views import cart_view, add_item, delete_item, clear_cart   # <-- include clear_cart

urlpatterns = [
     path('', cart_view, name='cart-view'),
    path('add/', add_item, name='add-item'),
    path('delete/<int:index>/', delete_item, name='delete-item'),
    path('clear/', clear_cart, name='clear-cart'),
]
