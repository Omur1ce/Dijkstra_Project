from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from map.cookies import cookies_test2
from map.cookies import cookies_test


urlpatterns = [
    path('', views.home, name='map'),
    path('about/',views.about, name='about'),
    path('dijkstra/',views.dijkstra),
    path('collect/',views.collect),
    path('test/', cookies_test2),
    path('sus/',views.setcookie),
    path('zezo/',views.zezo),
    path('result/',views.result),
    path('adder/<int:num>/', views.adder),
    path('pdf', views.pdf),
    path('saved/', views.saved, name='blog-saved'),
    path('save/',views.save),
    path('test2/', views.test2)
]

urlpatterns += staticfiles_urlpatterns()
path('your-name/', views.adder)