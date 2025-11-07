from django.urls import path
from .views import AccountCreateView, AccountUpdateView

urlpatterns = [
    # Rota para a página de registro de novos usuários
    path('signup/', AccountCreateView.as_view(), name='signup'),
    # Usar a classe importada diretamente (AccountUpdateView), não 'views.AccountUpdateView'
    path('account/<int:pk>/edit/', AccountUpdateView.as_view(), name='account_edit'),
]