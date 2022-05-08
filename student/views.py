from django.shortcuts import render, HttpResponse, redirect
from .models import *


# Create your views here.

def index(request):
    student_list = Student.objects.all()

    return render(request, "student/index.html", {"student_list": student_list})


def add_student(request):
    if request.method == "GET":
        class_list = Clas.objects.all()
        course_list = Course.objects.all()

        return render(request, "student/add_student.html", {"class_list": class_list, "course_list": course_list})
    else:
        print(request.POST)
        print(request.POST.dict())

        Student.objects.create(**request.POST.dict())
        return redirect("/student/index")
