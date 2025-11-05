from django import forms

from sac.models import Question

class QuestionForm(forms.ModelForm):
    class Meta: 
        model = Question
        fields = ('question_text', 'pub_date')
        labels = {
            'question_text': 'Texto da Pergunta',
            'pub_date': 'Data de Publicação',
        }
