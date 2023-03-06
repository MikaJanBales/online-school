from django.contrib import admin
from .models import Speakers, SpeakersWebinars, SpeakersCoursesBid, Webinars, Courses


# class SpeakersWebinarsInline(admin.TabularInline):
#     model = SpeakersWebinars
#     extra = 1


# class SpeakersAdmin(admin.ModelAdmin):
#     inlines = (SpeakersWebinarsInline,)


# class WebinarsAdmin(admin.ModelAdmin):
#     inlines = (SpeakersWebinarsInline,)


admin.site.register(Speakers)
admin.site.register(SpeakersWebinars)
admin.site.register(SpeakersCoursesBid)
admin.site.register(Webinars)
admin.site.register(Courses)
