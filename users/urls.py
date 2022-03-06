from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='users-register'),
    path('timetable/', views.timetable, name='users-timetable'),
    path('profile/<str:username>/', views.profile)
]