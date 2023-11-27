from django.urls import path
from dashboard.views import Dashboard, CategoryView


urlpatterns = [
    path('', Dashboard.as_view(), name="dashboard"),
    path('add-category', CategoryView.as_view(), name="add-category")
]