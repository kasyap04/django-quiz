from django.urls import path
from access.views import Login, Register, logout


urlpatterns = [
    path('login', Login.as_view(), name="login"),
    path('register', Register.as_view(), name="register"),
    path('logout', logout, name="logout"),
]