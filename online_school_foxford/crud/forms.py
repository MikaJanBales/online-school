from django.contrib.admin.helpers import Fieldset
from .models import Webinars, Courses, SpeakersWebinars, Speakers
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, TimeInput, ModelMultipleChoiceField, \
    CheckboxSelectMultiple


class SpeakersForm(ModelForm):
    class Meta:
        model = Speakers
        fields = ['name']


class WebinarsForm(ModelForm):
    speakers = ModelMultipleChoiceField(queryset=Speakers.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course_id'].empty_label = 'Курс не выбран'

    class Meta:
        model = Webinars
        fields = ['title_webinar', 'speakers', 'status', 'course_id', 'description']

        widgets = {
            'title_webinar': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название вебинара'
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


class SpeakersWebinarsForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['webinar_id'].empty_label = 'Вебинар не выбран'

    class Meta:
        model = SpeakersWebinars
        fields = ['date', 'time']
        # fields = ['speaker_id', 'webinar_id', 'date', 'time']

        widget = {
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Начало вебинара: yyyy-mm-dd hh:mm:ss'
            }),
            'time': TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Длительность вебинара: hh:mm:ss'
            }),
        }


