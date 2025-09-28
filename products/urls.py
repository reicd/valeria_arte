from django.urls import path
from products.views import (
    index, about, product_create, ProductUpdateView, ProductDeleteView
)


# Lista de caminhos (urls) do app products
urlpatterns = [
    path('', index, name='products-index'),
    path('about/', about, name='products-about'),
    path('criar_produto/', product_create, name='product_add'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]