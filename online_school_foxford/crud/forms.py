from .models import Webinars, Courses
from django.forms import ModelForm, TextInput, Textarea


class WebinarsForm(ModelForm):
    class Meta:
        model = Webinars
        fields = ['title_webinar', 'status', 'course_id', 'description']

        widgets = {
            'title_webinar': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название вебинара'
            }),
            'status': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Статус вебинара'
            }),
            'course_id': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название курса',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'О вебинаре',
            }),
        }


class CoursesForm(ModelForm):
    class Meta:
        model = Courses
        fields = ['title_course', 'description']

        widgets = {
            'title_course': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название курса'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'О курсе',
            }),
        }
