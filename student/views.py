from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.db.models import F, Q


# Create your views here.

def index(request):
    student_list = Student.objects.all()
    class_list = Clas.objects.all()
    return render(request, "student/index.html", {"student_list": student_list, "class_list": class_list})


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


def search(request):
    class_list = Clas.objects.all()
    print(request.POST)
    key_word = request.POST.dict().get("key_word")
    class_id = request.POST.dict().get("class_id")
    print(key_word)
    print(class_id, type(class_id))
    if class_id == "" and key_word == "":
        return redirect("/student/index")
    if class_id and key_word:
        student_list = Student.objects.filter(Q(name__contains=key_word) & Q(clas_id=class_id))
        return render(request, "student/index.html",
                      {"student_list": student_list, "class_list": class_list, "key_word": key_word,
                       "class_id": int(class_id)})
    else:
        if not key_word:
            student_list = Student.objects.filter(clas_id=class_id)
            return render(request, "student/index.html",
                          {"student_list": student_list, "class_list": class_list, "key_word": key_word,
                           "class_id": int(class_id)})
        else:
            student_list = Student.objects.filter(name__contains=key_word)
            return render(request, "student/index.html",
                          {"student_list": student_list, "class_list": class_list, "key_word": key_word})
