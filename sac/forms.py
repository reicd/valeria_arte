from django import forms

from sac.models import Question

class QuestionForm(forms.ModelForm):
    class Meta: 
        model = Question
        fields = ('question_text', 'pub_date')
