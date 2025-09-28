from django.urls import path
from .views import AccountCreateView

urlpatterns = [
    # Rota para a página de registro de novos usuários
    path('signup/', AccountCreateView.as_view(), name='signup'),
]