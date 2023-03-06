from django.urls import path
from . import views

urlpatterns = [
    path('webinars', views.WebinarsListView.as_view(), name='webinars'),
    path('courses', views.CoursesListView.as_view(), name='courses'),
    path('webinar_create', views.webinar_create_view, name='webinar_create'),
    path('course_create', views.CoursesCreateView.as_view(), name='course_create'),
    path('webinars/<int:pk>', views.WebinarsDetailView.as_view(), name='webinar_detail'),
    path('courses/<int:pk>', views.CoursesDetailView.as_view(), name='course_detail'),
    path('webinars/<int:pk>/update', views.WebinarsUpdateView.as_view(), name='webinar_update'),
    path('courses/<int:pk>/update', views.CoursesUpdateView.as_view(), name='course_update'),
    path('webinars/<int:pk>/delete', views.WebinarsDeleteView.as_view(), name='webinar_delete'),
    path('courses/<int:pk>/delete', views.CoursesDeleteView.as_view(), name='course_delete'),
]
