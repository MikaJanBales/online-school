from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


def crud_home(request):
    webs = Articles.objects.order_by('-date')
    return render(request, 'crud/crud_home.html', {'webs': webs})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'crud/create.html', data)
