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


def delete_student(request, del_id):
    student = Student.objects.get(pk=del_id)
    if request.method == "GET":
        return render(request, "student/del_student.html", {"student": student})
    else:
        student.delete()
        return redirect("/student/index")


def edit_student(request, edit_id):
    student = Student.objects.get(pk=edit_id)
    class_list = Clas.objects.all()
    course_list = Course.objects.all()
    if request.method == "GET":
        return render(request, "student/edit_student.html",
                      {"student": student, "class_list": class_list, "course_list": course_list})
    else:
        course_id_list = request.POST.getlist("course_id_list")  # ['1', '5']
        data = request.POST.dict()
        data.pop("course_id_list")
        Student.objects.filter(pk=edit_id).update(**data)
        student.course.set(course_id_list)
        return redirect("/student/index")


def elective(request):
    course_list = Course.objects.all()

    print(request.POST)
    if request.method == "GET":
        return render(request, "student/course.html", {"course_list": course_list})
    else:
        student_id = 3
        student = Student.objects.get(pk=student_id)
        course_id_list = request.POST.getlist("course_id_list")
        student.course.set(course_id_list)
        return redirect("/student/index")
