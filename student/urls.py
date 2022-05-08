from django.urls import path
from .views import index, add_student

urlpatterns = [
    path('index/', index),
    path('add/', add_student),
]
