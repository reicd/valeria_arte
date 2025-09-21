from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from sac.models import Question

# Create your views here.
from django.http import HttpResponse
# Definir uma view baseada em função.
def index(request):
    # return HttpResponse("Hello, world. You're at the sac index.")
    aviso = 'Esta página é pública.'
    messages.warning(request, aviso)
    return render(request, 'index.html', {'titulo': 'Página Inicial'})
# Definir uma view baseada em função.
@login_required
def about(request):
    # return HttpResponse("This is the about page of the sac app.")
    question = Question.objects.all()
    context = {'all_questions': question}
    return render(request, 'sac/question.html', context)

