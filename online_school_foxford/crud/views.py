from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView, TemplateView

from .models import Webinars, Courses, SpeakersWebinars
from .forms import WebinarsForm, CoursesForm, SpeakersWebinarsForm, SpeakersForm


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


# def webinar_create_view(request):
#     if request.method == 'POST':
#         speakers_webinars_form = SpeakersWebinarsForm(request.POST, prefix="speakers_webinars")
#         webinars_form = WebinarsForm(request.POST, prefix="webinars")
#         if speakers_webinars_form.is_valid() and webinars_form.is_valid():
#             print("all validation passed")
#             webinars = webinars_form.save()
#             speakers_webinars_form.cleaned_data["webinar_id"] = webinars
#             # speakers_webinars_form.save()
#             return HttpResponseRedirect('webinars')
#         else:
#             print("failed")
#     else:
#         speakers_webinars_form = SpeakersWebinarsForm(prefix="speakers_webinars")
#         webinars_form = WebinarsForm(prefix="webinars")
#     return render(request, 'crud/webinar_create.html', {
#         'speakers_webinars_form': speakers_webinars_form,
#         'webinars_form': webinars_form,
#     })

def webinar_create_view(request):
    webinars_form = WebinarsForm(request.POST or None)
    speakers_webinars_form = SpeakersWebinarsForm(request.POST or None)
    speakers_form = SpeakersForm(request.POST or None)
    context = {
        'webinars_form': webinars_form,
        'speakers_webinars_form': speakers_webinars_form,
        'speakers_form': speakers_form,
    }
    if speakers_webinars_form.is_valid() and webinars_form.is_valid() and speakers_form.is_valid():
        parent = webinars_form.save(commit=False)
        parent.save()
        child = speakers_webinars_form.save(commit=False)
        child.webinar_id = parent
        child.save()

        parent_2 = speakers_form.save(commit=False)
        parent_2.save()
        child_2 = speakers_webinars_form.save(commit=False)
        child_2.speaker_id = parent_2
        child_2.save()
    return render(request, 'crud/webinar_create.html', context)


class CoursesCreateView(CreateView):
    form_class = CoursesForm
    template_name = 'crud/course_create.html'


class WebinarsDetailView(DetailView):
    model = SpeakersWebinars
    template_name = 'crud/webinars_details_view.html'
    context_object_name = 'speakers_webinars'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['speakerswebinars'] = SpeakersWebinars.objects.all()
    #
    #     return context


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
