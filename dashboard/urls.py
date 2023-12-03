from django.urls import path
from dashboard.views import Dashboard, CategoryView, QuestionsView, editCategory, showAllCategories, showAllQuestions


urlpatterns = [
    path('', Dashboard.as_view(), name="dashboard"),
    path('category', CategoryView.as_view(), name="category"),
    path('edit-category', editCategory, name="edit-category"),
    path('question', QuestionsView.as_view(), name="question"),
    path('question', QuestionsView.as_view(), name="question"),
    path('view-questins', showAllCategories, name="view-questins"),
    path('view-questins/<cat_id>', showAllQuestions, name="view-questins"),
]