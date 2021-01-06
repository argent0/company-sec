from django import forms
from django.forms import ModelForm, ModelChoiceField

from website.models import Evaluation, EvaluationTarget, AnswerChoice

#class DashboardForm(forms.Form):
#    evaluation_id = forms.ChoiceField()

class DashboardForm(forms.Form):
    evaluation_id = forms.ModelChoiceField(queryset=Evaluation.objects.all())

class EvaluationTargetForm(forms.Form):
    evaluation_target = forms.ModelChoiceField(queryset=EvaluationTarget.objects.all())
    company = forms.CharField(max_length=200)
    duty = forms.CharField(max_length=200)

class QuestionAnswerForm(forms.Form):
    answer = forms.ChoiceField(choices=AnswerChoice.choices)
