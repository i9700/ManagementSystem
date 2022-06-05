# Generated by Django 3.2 on 2022-06-05 12:04

from django.db import migrations, models
import django.db.models.deletion
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_clas_course_student_studentdetail_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(default='/avatar/default.png', upload_to=student.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='stu',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]