from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="Texto da pergunta")
    pub_date = models.DateTimeField("Data de publicação")

    class Meta:
        verbose_name = "Pergunta"
        verbose_name_plural = "Perguntas"
