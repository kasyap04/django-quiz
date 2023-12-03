from django.urls import path
from startquiz import views

urlpatterns = [
    path('', views.StartQuick.as_view(), name="index"),
    path('<qstn_id>', views.StartQuick.as_view(), name="index"),
]