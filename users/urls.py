from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.about, name='users-register'),
    path('timetable/', views.about, name='users-timetable'),
]