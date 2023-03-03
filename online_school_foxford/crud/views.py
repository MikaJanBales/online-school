from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView

from .models import Webinars, Courses
from .forms import WebinarsForm, CoursesForm


class WebinarsListView(ListView):
    model = Webinars
    template_name = 'crud/webinars.html'
    context_object_name = 'webinars'


class CoursesListView(ListView):
    model = Courses
    template_name = 'crud/courses.html'
    context_object_name = 'courses'


class WebinarsCreateView(CreateView):
    form_class = WebinarsForm
    template_name = 'crud/webinar_create.html'


class CoursesCreateView(CreateView):
    form_class = CoursesForm
    template_name = 'crud/course_create.html'


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
