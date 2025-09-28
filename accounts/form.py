from django import forms 
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountSignupForm(forms.ModelForm):
    password = forms.CharField(
        label='Senha',
        max_length=50,
        widget=forms.PasswordInput() 
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'data_nascimento', 'telefone', 'endereco', 'cidade', 'estado', 'pais', 'cep', 'cpf', 'password',)
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date', }),
        }