from django.shortcuts import render


def book_detail(request):
    book = {
        'title': 'Война и мир',
        'author': 'Лев Толстой',
        'year': 1869,
    }
    return render(request, 'book_detail.html', {'book': book})

