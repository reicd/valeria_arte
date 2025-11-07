from django import forms

from sac.models import Question

class QuestionForm(forms.ModelForm):
    class Meta: 
        model = Question
        fields = ('question_text', 'pub_date')
        widgets = {
            'question_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'pub_date': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local'
                },
                format='%Y-%m-%dT%H:%M'
            ),
        }
        labels = {
            'question_text': 'Pergunta',
            'pub_date': 'Data de Publicação',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.pub_date:
            # Formata a data para o formato aceito pelo input datetime-local
            self.initial['pub_date'] = self.instance.pub_date.strftime('%Y-%m-%dT%H:%M')
