from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers  import make_password
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()
from accounts.form import AccountSignupForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class AccountCreateView(CreateView):
    model = User
    form_class = AccountSignupForm
    template_name = 'registration/signup_form.html'
    success_url = reverse_lazy('login')
    success_message = 'Conta criada com sucesso!'

    def form_valid(self, form) -> HttpResponse:
        form.instance.password = make_password(form.instance.password)
        form.save()
        messages.success(self.request, self.success_message)

        return super(AccountCreateView, self).form_valid(form)
class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/user_form.html'
    fields = ['first_name', 'last_name', 'email',  'imagem']
    success_url = reverse_lazy('about')
    success_message = 'Perfil atualizado com sucesso!'
        #Editar o próprio perfil
    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        user = self.request.user
        if user is None or not user.is_authenticated or user.id != user_id:
            return User.objects.none()
        return User.objects.filter(id=user_id)
    def form_valid(self, form) -> HttpResponse:
        messages.success(self.request, self.success_message)
        return super(AccountUpdateView, self).form_valid(form)