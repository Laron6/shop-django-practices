from django.shortcuts import render


def get_privet(request):
    return render(request, 'privet.html', {'message': 'Привет, мир!'})
