from django.contrib import admin
from website.models import Question, Evaluation, EvaluationTarget
from website.models import EvaluationResult

# Register your models here.

admin.site.register(Question)
admin.site.register(Evaluation)
admin.site.register(EvaluationTarget)
admin.site.register(EvaluationResult)
