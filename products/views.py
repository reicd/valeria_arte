from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

@login_required
def product_create(request):
    """
    View baseada em função para criar um novo produto.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso.')
            return redirect('products-index') # Redireciona para a lista de produtos
    else:
        form = ProductForm()
    
    context = {'form': form}
    return render(request, 'produtos/product_form.html', context)
class ProductsCreateView(CreateView):
    model = Product
    template_name = 'products/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('products-index')

    def form_valid(self, form):
        messages.success(self.request, 'Produto criado com sucesso.')
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'produtos/product_form.html' # Reutiliza o mesmo formulário da criação
    success_url = reverse_lazy('products-index')

    def form_valid(self, form):
        messages.success(self.request, 'Produto atualizado com sucesso.')
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'produtos/product_confirm_delete.html' # Template de confirmação
    success_url = reverse_lazy('products-index')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'Produto excluído com sucesso.')
        return super().post(request, *args, **kwargs)
