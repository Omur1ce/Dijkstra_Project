from django.shortcuts import render
from django import forms

def cookies_test(request):
    template_name = 'cookies.html'
    current_name = "Rigatoni"  # default name
    if request.method == 'GET':
        if 'name' in request.COOKIES:
            current_name = request.COOKIES['name']
    elif request.method == 'POST':
        current_name = request.POST.get('name')
    response = render(request, 'test.html', {
        "current_name": current_name
    })
    response.set_cookie('name', current_name)

    return response


def cookies_test2(request):
    template_name = 'cookies.html'
    current_colour = "Oxaeaeae"  # default colour
    if request.method == 'GET':
        if 'colour' in request.COOKIES:
            current_colour = request.COOKIES['colour']
            print("GET:colour:" + request.COOKIES.get('colour'))
    elif request.method == 'POST':
        current_colour = request.POST.get('colour')
    response = render(request, 'test.html', {
        "current_colour": current_colour
    })
    response.set_cookie('colour', current_colour)

    return response
