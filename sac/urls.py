from django.urls import path
from sac.views import ( index, about, QuestionCreateView, question_create,
QuestionUpdateView, question_update, 
)



#Lista de caminhos (urls) do app sac
urlpatterns = [
    #path('rota/', view, name='nome_da_rota'),
    #Exemplo:
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('pergunta/add', QuestionCreateView.as_view(), name="sac_add"),
    path('pergunta/create',question_create, name= "question_create" ),
    path('pergunta/<int:pk>/edit', QuestionUpdateView.as_view(), name="sac_edit"),
    path('pergunta/<int:pk>/update', question_update, name="question_update" ),
 ]