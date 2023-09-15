from django.contrib import admin
from .models import Student, Teacher


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','gender','city','inclass','roll','age']
    

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name","gender","city","age"]    