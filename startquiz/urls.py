from django.urls import path
from startquiz import views

urlpatterns = [
    path('', views.StartQuick.as_view(), name="index"),
    path('save', views.ResultView.as_view(), name="save-result"),
    
    path('<cat_id>', views.StartQuick.as_view(), name="category"),
    path('<cat_id>/<index>', views.StartQuick.as_view(), name="category-questions"),
]