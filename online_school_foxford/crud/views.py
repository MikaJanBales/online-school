from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView

from .models import Webinars, Courses
from .forms import WebinarsForm, CoursesForm, SpeakersWebinarsForm


class WebinarsListView(ListView):
    model = Webinars
    template_name = 'crud/webinars.html'
    context_object_name = 'webinars'


# def webinars(request):
#     webs = Webinars.objects.all()
#     return render(request, 'crud/webinars.html', {'webinars': webs})

class CoursesListView(ListView):
    model = Courses
    template_name = 'crud/courses.html'
    context_object_name = 'courses'


def webinar_create_view(request):
    if request.method == 'POST':
        speakers_webinars_form = SpeakersWebinarsForm(request.POST, prefix="speakers_webinars")
        webinars_form = WebinarsForm(request.POST, prefix="webinars")
        if speakers_webinars_form.is_valid() and webinars_form.is_valid():
            print("all validation passed")
            webinars = webinars_form.save()
            speakers_webinars_form.cleaned_data["webinar_id"] = webinars

            return HttpResponseRedirect('webinars')
        else:
            print("failed")
    else:
        speakers_webinars_form = SpeakersWebinarsForm(prefix="speakers_webinars")
        webinars_form = WebinarsForm(prefix="webinars")
    return render(request, 'crud/webinar_create.html', {
        'speakers_webinars_form': speakers_webinars_form,
        'webinars_form': webinars_form,
    })


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
