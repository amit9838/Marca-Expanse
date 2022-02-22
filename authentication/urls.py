from multiprocessing.spawn import import_main_path
from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('register/',RegistrationView.as_view(), name = "register"),
    path('login/',LoginView.as_view(), name = "login"),
]
