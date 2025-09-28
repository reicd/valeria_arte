from django.urls import path
from products.views import index, about, ProductsCreateView, question_create


# Lista de caminhos (urls) do app products
urlpatterns = [
    #path('rota/', view, name='nome_da_rota'),
    #Exemplo:
    path('', index, name='products-index'),
    path('about/', about, name='products-about'),
    path('product/add/', ProductsCreateView.as_view(), name='product_add'),
    path('product/new/', question_create, name='product_new'),
]