from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Product
from products.forms import ProductForm

# Create your views here.
@login_required
def index(request):
    """
    View para listar os produtos.
    """
    products = Product.objects.all()
    context = {'all_products': products}
    return render(request, 'produtos/manipular.html', context)

# Views de placeholder para evitar erros de importação nas URLs.
# O ideal é que elas tenham sua própria lógica ou sejam removidas das URLs se não forem usadas.
def about(request):
    return redirect('about') # Redireciona para a view 'about' principal

def question_create(request):
    return redirect('index') # Redireciona para a página inicial

class ProductsCreateView(CreateView):
    model = Product
    template_name = 'products/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('products-index')

    def form_valid(self, form):
        messages.success(self.request, 'Produto criado com sucesso.')
        return super().form_valid(form)
