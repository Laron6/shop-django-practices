from django.contrib import admin
from .models import Student, Teacher, Course


# Настройка отображения модели Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ('name',)  # Добавляем поиск по имени студента


# Настройка отображения модели Teacher
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)  # Добавляем поиск по имени учителя


# Настройка отображения модели Course
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher')  # Отображаем название курса и учителя
    search_fields = ('title', 'teacher__name')  # Добавляем поиск по названию курса и имени учителя
    filter_horizontal = ('students',)  # Для удобного выбора студентов
