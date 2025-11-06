from django import forms

from sac.models import Question

class QuestionForm(forms.ModelForm):
    class Meta: 
        model = Question
        fields = ('question_text', 'pub_date')
        widgets = {
            'question_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'pub_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
        labels = {
            'question_text': 'Pergunta',
            'pub_date': 'Data de Publicação',
        }
