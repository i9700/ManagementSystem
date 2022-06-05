from django.urls import path, re_path
from .views import index, add_student, delete_student, edit_student, elective, search, stu_excel

urlpatterns = [
    path('index/', index),
    path('add/', add_student),
    # 选课
    path('elective/', elective),
    re_path('delete/(\d+)', delete_student),
    re_path('edit/(\d+)', edit_student),
    # 筛选
    path('search/', search),

    # 通过excel表格批量导入数据
    path('stu_excel/', stu_excel)
]
