from django.shortcuts import render


def index(request):
    data = {
        'title': 'chupapupsik',
        'values': ['red', 'blue', 'white'],
        'obj': {
            'car': 'mers',
            'age': '20',
            'hobby': 'football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
