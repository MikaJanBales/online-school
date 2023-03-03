from django.contrib import admin
from .models import Speakers, SpeakersWebinars, SpeakersCoursesBid, Webinars, Courses

admin.site.register(Speakers)
admin.site.register(SpeakersWebinars)
admin.site.register(SpeakersCoursesBid)
admin.site.register(Webinars)
admin.site.register(Courses)
