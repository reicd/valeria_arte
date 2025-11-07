from django.forms import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
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
    form_class = QuestionForm
    success_url = reverse_lazy('about')
    sucess_message ='Pergunta criada com sucesso.'
    
    def form_valid(self, form):
        messages.success(self.request, self.sucess_message)
        return super(QuestionCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(QuestionCreateView, self).get_context_data(**kwargs)
        context['form_title'] = 'Criar Pergunta'
        return context

@login_required
def question_create(request):
    context = {}
    form = QuestionForm(request.POST or None, request.FILES or None)
    context['form'] = form
    context['form_title'] = 'Criar Pergunta'
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Pergunta criada com sucesso')
            return redirect("about")
    
    return render(request, 'sac/question_form.html', context)

class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    template_name = 'sac/question_form.html'
    form_class = QuestionForm
    success_url = reverse_lazy('about')
    sucess_message ='Pergunta atualizada com sucesso.'
    
    def form_valid(self, form):
        messages.success(self.request, self.sucess_message)
        return super(QuestionUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(QuestionUpdateView, self).get_context_data(**kwargs)
        context['form_title'] = 'Editando uma pergunta'
        return context
    
@login_required
def question_update(request, pk):
    context = {}
    question = get_object_or_404(Question, pk=pk)
    form = QuestionForm(request.POST or None, request.FILES or None, instance=question)
    context['form'] = form
    context['form_title'] = 'Editando uma pergunta'
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Pergunta atualizada com sucesso')
            return redirect("about")
    
    return render(request, 'sac/question_form.html', context)

class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'sac/question_confirm_delete.html'
    success_url = reverse_lazy('about')
    sucess_message ='Pergunta deletada com sucesso.'
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.sucess_message)
        return super(QuestionDeleteView, self).delete(request, *args, **kwargs)
@login_required
def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    
    if request.method == "POST":
        question.delete()
        messages.success(request, 'Pergunta deletada com sucesso')
        return redirect("about")
    
    context = {'object': question}
    return render(request, 'sac/question_confirm_delete.html', context)
class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'sac/question_detail.html'
    context_object_name = 'question'
