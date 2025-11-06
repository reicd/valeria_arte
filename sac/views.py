from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from sac.models import Question
from sac.forms import QuestionForm

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

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    template_name = 'sac/question_form.html'
    fields = ('question_text', 'pub_date')
    success_url = reverse_lazy('index')
    sucess_message ='Pergunta criada com sucesso.'
    
    def form_valid(self, form):
        messages.success(self.request, self.sucess_message)
        return super(QuestionCreateView, self).form_valid(form)
@login_required
def question_create(request):
    context = {}
    form = QuestionForm(request.POST or None, request.FILES or None)
    context['form'] = form
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request= 'Pergunta criada com sucesso')
            return redirect("index")
    
    return render(request, 'sac/question_form.html', context)