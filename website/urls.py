from django.urls import path, include
from website.views import DashboardView, evaluation_new_form_view, evaluation_create_view
from website.views import EvaluationResultView, EvaluationResultListView

app_name = 'website'

urlpatterns = [
        path('', DashboardView.as_view(), name='dashboard'),
        path('evaluation/<int:pk>/', EvaluationResultView.as_view(), name='evaluation'),
        path('evaluation/new', evaluation_new_form_view, name='evaluation-new'),
        path('evaluation/create', evaluation_create_view, name='evaluation-create'),
        path('evaluation/', EvaluationResultListView.as_view(), name='evaluation-list'),
]
