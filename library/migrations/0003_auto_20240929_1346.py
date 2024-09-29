from django.db import migrations


def add_initial_data(apps, schema_editor):
    # Получаем модели через apps.get_model (нельзя импортировать напрямую)
    Student = apps.get_model('university', 'Student')
    Teacher = apps.get_model('university', 'Teacher')
    Course = apps.get_model('university', 'Course')
    Author = apps.get_model('library', 'Author')
    Publisher = apps.get_model('library', 'Publisher')
    Book = apps.get_model('library', 'Book')

    # Создание записей для студентов
    student1 = Student.objects.create(name='Александр Иванов', age=20)
    student2 = Student.objects.create(name='Мария Петрова', age=22)
    student3 = Student.objects.create(name='Иван Сидоров', age=21)

    # Создание записей для учителей
    teacher1 = Teacher.objects.create(name='Николай Сергеев')
    teacher2 = Teacher.objects.create(name='Ольга Васильева')

    # Создание записей для курсов
    course1 = Course.objects.create(title='Математика', teacher=teacher1)
    course2 = Course.objects.create(title='Физика', teacher=teacher2)

    # Добавление студентов на курсы
    course1.students.add(student1, student2)
    course2.students.add(student2, student3)

    # Создание записей для авторов
    author1 = Author.objects.create(name='Лев Толстой', date_of_birth='1828-09-09', gender='Мужчина')
    author2 = Author.objects.create(name='Фёдор Достоевский', date_of_birth='1821-11-11', gender='Мужчина')

    # Создание записей для издателей
    publisher1 = Publisher.objects.create(name='Издательство АСТ')
    publisher2 = Publisher.objects.create(name='Эксмо')

    # Создание записей для книг и добавление связей
    book1 = Book.objects.create(title='Война и мир', year=1869, author=author1)
    book2 = Book.objects.create(title='Преступление и наказание', year=1866, author=author2)

    # Добавление издателей к книгам (связь многие-ко-многим)
    book1.publisher.add(publisher1, publisher2)
    book2.publisher.add(publisher2)


class Migration(migrations.Migration):
    dependencies = [
        ('library', '0002_author_publisher_alter_book_author_book_publisher'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),  # Запуск функции для добавления данных
    ]
