from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

from django.contrib.postgres.fields import ArrayField, JSONField

QUESTION_HASH_DIGITS = 4

# Create your models here.

class Evaluation(models.Model):
    """ The evaluation model """
    # When was it created
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    """ The question model """
    creation_date = models.DateTimeField(auto_now_add=True)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)

    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class EvaluationTarget(models.Model):
    """ A person that could potentially be evaluated """
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    name = models.CharField(max_length=100)
    personal_id_number = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class EvaluationResult(models.Model):
    """ The result of an evaluation """
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    evaluation_target = models.ForeignKey(EvaluationTarget, on_delete=models.PROTECT)
    target_company = models.CharField(max_length=100)
    target_duty = models.CharField(max_length=100)

    results = JSONField()

class AnswerChoice(models.TextChoices):
    """ Possible answers """
    ACCEPTABLE = 'ACCEPTABLE'
    UNACCAPTABLE = 'UNACCAPTABLE'
