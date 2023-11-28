from django.urls import path
from dashboard.views import Dashboard, CategoryView, QuestionsView


urlpatterns = [
    path('', Dashboard.as_view(), name="dashboard"),
    path('category', CategoryView.as_view(), name="category"),
    path('question', QuestionsView.as_view(), name="question"),
]