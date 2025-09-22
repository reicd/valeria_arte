from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # You can add additional fields here if needed
    data_nascimento = models.DateField("Data de Nascimento", 
    null=True, 
    blank=True)
    telefone = models.CharField("Telefone",max_length=15, null=True, blank=True)
    endereco = models.CharField("Endereço",max_length=255, null=True, blank=True)
    cidade = models.CharField("Cidade",max_length=100, null=True, blank=True)
    estado = models.CharField("Estado",max_length=100, null=True, blank=True)
    pais = models.CharField("País",max_length=100, null=True, blank=True)
    cep = models.CharField("CEP",max_length=8, null=True, blank=True)
    cpf = models.CharField("CPF",max_length=11, null=True, blank=True)