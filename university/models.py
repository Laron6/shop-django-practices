from django.db import models


# Модель Student
class Student(models.Model):
    name = models.CharField(max_length=100)  # Имя студента
    age = models.IntegerField()  # Возраст студента

    def __str__(self):
        return self.name


# Модель Teacher
class Teacher(models.Model):
    name = models.CharField(max_length=100)  # Имя учителя

    def __str__(self):
        return self.name


# Модель Course
class Course(models.Model):
    title = models.CharField(max_length=200)  # Название курса
    students = models.ManyToManyField(Student)  # Связь многие-ко-многим с Student
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Связь один-ко-многим с Teacher

    def __str__(self):
        return self.title
