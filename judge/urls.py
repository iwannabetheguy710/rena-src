from django.urls import path

from . import views

urlpatterns = [
	path('problem/<int:problem_id>/submission/', views.submission_page, name="submission"),
	path('problem/<int:problem_id>/submission/judge/', views.submission_judge_page, name="submission judge"),
]