from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers  import make_password
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth import get_user_model
User = get_user_model()

from accounts.form import AccountSignupForm


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
