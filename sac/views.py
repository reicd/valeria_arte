from django.shortcuts import render

from sac.models import Question

# Create your views here.
from django.http import HttpResponse
# Definir uma view baseada em função.
def index(request):
    # return HttpResponse("Hello, world. You're at the sac index.")
    return render(request, 'index.html', {'titulo': 'Página Inicial'})
# Definir uma view baseada em função.
def about(request):
    # return HttpResponse("This is the about page of the sac app.")
    question = Question.objects.all()
    context = {'all_questions': question}
    return render(request, 'sac/question.html', context)

