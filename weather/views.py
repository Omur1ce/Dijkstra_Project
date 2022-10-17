from django.shortcuts import render
import requests
from .models import City
from weather.forms import CityForm
 
def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5a872e14b602c48f4fbe12ee7cf1925e'
 
    cities = City.objects.all() #return all the cities in the database
    weather_data = []
 
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if valid
 
    form = CityForm()
 
    weather_data = []
 
    for city in cities:
        response = requests.get(url.format(city))
        if response.status_code == 404:
         continue
        city_weather = response.json()
 
   
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
              }
 
        weather_data.append(weather) #add the data for the current city into our list
 
    context = {'weather_data' : weather_data, 'form' : form}
 
    return render(request, 'weather/index.html', context) #returns the index.html template

