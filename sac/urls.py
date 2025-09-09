from django.urls import path
from sac.views import index, about

#Lista de caminhos (urls) do app sac
urlpatterns = [
    #path('rota/', view, name='nome_da_rota'),
    #Exemplo:
    path('index/', index, name='sac-index'),
    path('about/', about, name='sac-about'),    
]