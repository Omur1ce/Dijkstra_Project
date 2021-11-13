from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from map.cookies import cookies_test

urlpatterns = [
    path('', views.home, name='map'),
    path('about/',views.about, name='about'),
    path('dijkstra/',views.dijkstra),
    path('collect/',views.collect),
    path('test/',cookies_test,)
]

urlpatterns += staticfiles_urlpatterns()
