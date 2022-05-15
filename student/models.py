from django.db import models


# Create your models here.

class Student(models.Model):
    SEX_CHOICES = (
        (0, "男"),
        (1, "女"),
    )
    name = models.CharField(max_length=32, unique=True, verbose_name="姓名")
    age = models.IntegerField(null=True, verbose_name="年龄")
    sex = models.SmallIntegerField(choices=SEX_CHOICES)
    birthday = models.DateField()

    clas = models.ForeignKey(to="Clas", related_name="student_list", on_delete=models.CASCADE,
                             db_constraint=False)  # 班级关联
    course = models.ManyToManyField("Course", related_name="students", db_table="db_stu2course", )  # 课程关联

    stu_detail = models.OneToOneField("StudentDetail", related_name="stu", on_delete=models.CASCADE, null=True,
                                      blank=True)

    class Meta:
        db_table = "db_student"

    def __str__(self):
        return self.name


class Clas(models.Model):
    name = models.CharField(max_length=32, verbose_name="班级名称")

    class Meta:
        db_table = "db_class"


class Course(models.Model):
    title = models.CharField(max_length=32, verbose_name="课程名称")
    credit = models.IntegerField(verbose_name="学分", default=3)
    teacher = models.CharField(max_length=32, verbose_name="老师", null=True)
    classTime = models.CharField(max_length=32, verbose_name="上课时间", null=True)
    classAddr = models.CharField(max_length=32, verbose_name="上课地点", null=True)

    class Meta:
        db_table = "db_course"

    def __str__(self):
        return self.title


class StudentDetail(models.Model):
    tel = models.CharField(max_length=11)
    addr = models.CharField(max_length=32)

    class Meta:
        db_table = "db_stu_detail"
