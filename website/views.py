import logging
import urllib

from django.forms import formset_factory, ModelChoiceField

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import View, TemplateView, FormView, DetailView, ListView
from django.views.generic.list import MultipleObjectTemplateResponseMixin
from django.views.decorators.http import require_http_methods

from website.models import Evaluation, Question, EvaluationTarget, EvaluationResult
from website.forms import DashboardForm, QuestionAnswerForm, EvaluationTargetForm

from django.shortcuts import render, redirect, reverse

LOGGER = logging.getLogger(__name__)

# Create your views here.

class DashboardView(LoginRequiredMixin, FormView):
    login_url = 'accounts/login'
    template_name = 'website/dashboard.html'
    form_class = DashboardForm

@require_http_methods(["GET"])
@login_required(redirect_field_name='next', login_url='/accounts/login')
def evaluation_new_form_view(request):
    """ Sigh """
    #return render(request, 'website/evaluation.html', {'poll': p})
    evaluation_id = request.GET['evaluation_id']
    evaluation = Evaluation.objects.get(pk=evaluation_id)

    # Prepare the questions formset
    questions = Question.objects.filter(evaluation=evaluation_id)
    form_class = formset_factory(QuestionAnswerForm, extra=questions.count())
    formset = form_class(prefix='answer')
    for form, question in zip(formset, questions.iterator()):
        form.fields['answer'].label = question.text

    # Prepare the evaluee form
    evaluee_form = EvaluationTargetForm()
    return render(
        request,
        'website/evaluation.html',
        {'evaluation': evaluation,
         'form': formset,
         'evaluee_form': evaluee_form,
        })

@require_http_methods(["POST"])
@login_required(redirect_field_name='next', login_url='/accounts/login')
def evaluation_create_view(request):
    """ Save an evaluation result """
    LOGGER.error(repr(request.POST))

    # retrieve the evaluation target

    evaluation_target_id = request.POST['evaluation_target']
    evaluation_target_query = EvaluationTarget.objects.filter(pk=evaluation_target_id)
    assert evaluation_target_query.count() == 1 #there should be only one
    evaluation_target = evaluation_target_query.get()

    # # check if the questions have already been asked.

    # ## Retrive the evaluation

    evaluation_id = request.POST['evaluation']
    evaluation_query = Evaluation.objects.filter(pk=evaluation_id)
    assert evaluation_query.count() == 1 #there should be only one
    evaluation = evaluation_query.get()

    # ## Retrive the evaluation questions
    questions_query = Question.objects.filter(evaluation=evaluation.pk)

    # All questoins need answers
    n_posted_answers = request.POST['answer-TOTAL_FORMS']
    assert n_posted_answers == str(questions_query.count())

    # Prepare the answers formset
    form_class = formset_factory(QuestionAnswerForm, extra=questions_query.count())
    formset = form_class(request.POST, prefix='answer')

    if formset.is_valid():
        # check the evaluation target form
        evaluation_target_form = EvaluationTargetForm(request.POST)
        if evaluation_target_form.is_valid():
            results = []
            for question, answer in zip(questions_query, formset.cleaned_data):
                answer['question'] = str(question)
                results.append(answer)
            LOGGER.error(results)

            # save the evaluation.
            new_evaluation_result = EvaluationResult.objects.create(
                owner=request.user,
                evaluation_target=evaluation_target_form.cleaned_data['evaluation_target'],
                target_company=evaluation_target_form.cleaned_data['company'],
                target_duty=evaluation_target_form.cleaned_data['duty'],
                results=results)

            return redirect(reverse(
                'website:evaluation',
                kwargs={'pk': new_evaluation_result.id}))

    raise Exception("Debug Exception")

class EvaluationResultView(LoginRequiredMixin, DetailView):
    """ View one evaluation result """
    model = EvaluationResult
    context_object_name = 'result'
    template_name = 'website/evaluation.detail.html'

    def get_context_data(self, **kwargs):
        """ Sigh """
        context = super().get_context_data(**kwargs)
        return context

class EvaluationResultListView(LoginRequiredMixin, ListView):
    """ Sigh """
    model = EvaluationResult
    context_object_name = 'results'
    template_name = 'website/evaluation.results.html'
