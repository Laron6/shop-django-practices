from django.contrib import admin
from .models import Student, Teacher, Course


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher')
    filter_horizontal = ('students',)  # Удобный выбор студентов
