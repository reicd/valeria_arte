from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'stock')
        labels = {
            'name': 'Nome do Produto',
            'description': 'Descrição',
            'price': 'Preço',
            'stock': 'Estoque',
        }