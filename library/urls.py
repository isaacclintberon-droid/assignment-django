from django.urls import path
from . import views

urlpatterns = [
    path("", views.library_home, name="library_home"),
]
