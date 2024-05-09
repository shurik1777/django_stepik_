from django.shortcuts import render


def index(request):
    dic = {
        'title': 'Главная страница',
        'values': ['some', 'free', 'ane'],
        'obj': {
            'a': "fff",
            'b': 2,
            'c': 3,
        }
    }
    return render(request, 'main/index.html', dic)


def about(request):
    return render(request, 'main/about.html')
