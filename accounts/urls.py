from django.urls import path
from .views import AccountCreateView, AccountUpdateView

urlpatterns = [
    # Rota para a página de registro de novos usuários
    path('signup/', AccountCreateView.as_view(), name='signup'),
    path('account/<int:pk>/edit/', AccountUpdateView.as_view(), name='account_edit'),
]