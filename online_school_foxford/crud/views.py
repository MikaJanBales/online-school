from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import Webinars, Courses
from .forms import WebinarsForm, CoursesForm


def webinars(request):
    webs = Webinars.objects.all()
    return render(request, 'crud/webinars.html', {'webinars': webs})


def courses(request):
    crs = Courses.objects.all()
    return render(request, 'crud/courses.html', {'courses': crs})


def webinar_create(request):
    error = ''
    if request.method == 'POST':
        form = WebinarsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webinars')
        else:
            error = 'Форма была неверной'

    form = WebinarsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'crud/webinar_create.html', data)


def course_create(request):
    error = ''
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
        else:
            error = 'Форма была неверной'

    form = CoursesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'crud/course_create.html', data)


class WebinarsDetailView(DetailView):
    model = Webinars
    template_name = 'crud/webinars_details_view.html'
    context_object_name = 'webinars'


class CoursesDetailView(DetailView):
    model = Courses
    template_name = 'crud/courses_details_view.html'
    context_object_name = 'courses'


class WebinarsUpdateView(UpdateView):
    model = Webinars
    template_name = 'crud/webinar_update.html'

    form_class = WebinarsForm


class CoursesUpdateView(UpdateView):
    model = Courses
    template_name = 'crud/course_update.html'

    form_class = CoursesForm


class WebinarsDeleteView(DeleteView):
    model = Webinars
    success_url = '/crud/webinars'
    template_name = 'crud/webinar_delete.html'


class CoursesDeleteView(DeleteView):
    model = Courses
    success_url = 'crud/courses'
    template_name = 'crud/course_delete.html'

