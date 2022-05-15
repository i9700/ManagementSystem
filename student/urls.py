from django.urls import path, re_path
from .views import index, add_student, delete_student, edit_student,elective

urlpatterns = [
    path('index/', index),
    path('add/', add_student),
    path('elective/', elective),
    re_path('delete/(\d+)', delete_student),
    re_path('edit/(\d+)', edit_student),
]
