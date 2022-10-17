from django.shortcuts import render
from django.http import HttpResponse
import json
from urllib.request import urlopen
import urllib
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from map.forms import *
from textwrap import wrap

def results(request):
    #Dijkstra function here
    return render(request, result.html)

def saved(request):
    return render(request, 'saved.html', {'title': 'About'})

def save(request):
  src = request.POST.get('start')
  dest = request.POST.get('end')
  src.save
  dest.save
  return(render(request(saved.html)))

def pdf(request):
    #creating Bytestream Buffer
    buf = io.BytesIO()
    #creating a canvas
    c = canvas.Canvas(buf, pagesize = letter, bottomup=0)
    #creating a text object
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica", 14)

    content = [
        "Locations"
    ]
    wrapped_text = "\n".join(wrap(content, 80))
    content(wrapped_text)
    for line in content:
        textob.textLine(line)

    c.drawText(textob)
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename = 'direction_pdf')



def collect():
    return HttpResponse('<h1>ha</h1>')

def home(request):
    #form = InputForm(request.POST)
    #if form.isvalid():
      #  start = form.save()
     #   start.save()
   # context = {'form': form, 'start': start}
    return render(request, 'home.html')

def adder(request, num):
    number = num
    return HttpResponse(number + 1)


def name(request):
    return render(request,'name.html')

def about(request):
    def add():
        return 1
    return HttpResponse(add())


def dijkstra_page(request):
    response = HttpResponse("hellooo")
    response.set_cookie('graph', {'laidlawS': {'swimming': 100, 'astro': 100, 'mount': 135},
                                  'mount': {'laidlawS': 135, 'dining': 85},
                                  'swimming': {'laidlawS': 100},
                                  'astro': {'laidlawS': 100},
                                  'dining': {'mount': 85}
                                  })
    return response
3


def collect(request):
    url = "http://127.0.0.1:8000/"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return HttpResponse(data)


def insertcolor(request):
    if request.method == 'POST':
        if request.POST.get('colorname'):
            savecolor = Locations()
            savecolor = request.POST.get('colorname')
            savecolor.save()
            messages.success(request, 'Select Color Saved Successfully..!')
            return render(request, 'Index.html')
    else:
        return render(request, 'test.html')


def saveCriteria(request):
    if request.method == "POST":
        context = {}
        title = request.POST.get('quantity')
        print(title)
    return render(request, "test.html", context)


def test(request):
    response = HttpResponse("HELP")
    response.set_cookie('name', "Rigatoni")
    
    return HttpResponse(request, "test.html")

def test2(request):
    person = request.session.get("username")
    weather= "sunny"
    context= {
        'person': person,
        'weather': weather,
        }
    return render(request, 'test2.html', context)


def zezo(request):
    value = request.COOKIES.get('name')
    if value is None:
        pass
    else:
        return render(request, "home.html")


def setcookie(request):
    response = HttpResponse("sus")
    response.set_cookie("cookietest", "testvalue")
    return render(request, "test.html")

def setsession(request):
    request.session['src'] = 'laidlawS'

def dijkstra(request):
    def dijkstra(graph, src, dest, visited=[], distances={}, predecessors={}):

        graph1 = {'Laidlaw South': {'CCF Hut': 45, 'Astroturf': 100, 'Mount Olympus': 135},

                  'Mount Olympus': {'Laidlaw South': 135, 'Dining Hall': 85},

                  'Swimming Pool': {'CCF Hut': 40},

                  'CCF Hut': {'Swimming Pool': 40, 'Laidlaw South': 45, 'Chalmers East': 45},

                  'Astroturf': {'Laidlaw South': 100, 'The Arena': 80},

                  'The Arena': {'Astroturf': 80, 'Sports Hall': 30},

                  'Sports Hall': {'The Arena': 30, 'Napier': 50},

                  'Dining Hall': {'Mount Olympus': 85, 'Chalmers East': 60, 'Chalmers West': 90, 'Main Entrance': 50},

                  'Mappa Mundi': {'Chalmers East': 80, 'Napier': 10},

                  'Napier': {'Mappa Mundi': 10, 'Music': 40, 'Sports Hall': 50},

                  'Music': {'Napier': 40, 'Computing': 15},

                  'Computing': {'Music': 15, 'Art': 20},

                  'Art': {'Computing': 20, 'Gibson': 40},

                  'Gibson': {'Art': 40, 'Chalmers West': 35},

                  'Chalmers West': {'Gibson': 35, 'Chalmers East': 80, 'Dining Hall': 90},

                  'Chalmers East': {'Chalmers West': 80, 'Dining Hall': 60, 'Mappa Mundi': 80, 'CCF Hut': 45},

                  'Main Entrance': {'Dining Hall': 50, 'Pringle Centre': 135},

                  'Pringle Centre': {'Main Entrance': 135, 'Rifle Range': 50, 'Tennis Courts': 50},

                  'Rifle Range': {'Pringle Centre': 50, 'Pringle Staff Housing': 30, 'Pringle House': 20},

                  'Tennis Courts': {'Pringle Centre': 50},

                  'Pringle Staff Housing': {'Rifle Range': 50, 'Secret Garden': 10},

                  'Pringle Football Pitch': {'Pringle Centre': 30},

                  'Pringle House': {'Rifle Range': 20, 'Pringle Football Pitch': 30, 'Secret Garden': 40},

                  'Secret Garden': {'Pringle House': 40, 'Pringle Staff Housing': 10, 'The Stable': 60},

                  'The Stable': {'Secret Garden': 60, 'School Entrance': 75},

                  'School Entrance': {'The Stable': 75}

                  }

        # error prevention checks

        if src not in graph:
            raise TypeError('The root of the shortest path tree cannot be found')

        if dest not in graph:
            raise TypeError('The target of the shortest path cannot be found')

        if src == dest:

            # We build the shortest path and display it

            path = []

            pred = dest

            while pred != None:
                path.append(pred)

                pred = predecessors.get(pred, None)

            # reverses the array

            readable = path[0]

            for index in range(1, len(path)): readable = path[index] + ' ---> ' + readable

            time = distances[dest] // 1.4

            # prints it

            print('shortest path: ' + str(path))

            print("Directions: " + readable)

            print("Distance: " + str(distances[dest]) + 'm')

            print('Estimated time: ' + str(time) + 's')

        else:

            # if it is the initial  run, initializes the cost

            if not visited:
                distances[src] = 0

            # visit the neighbors

            for neighbor in graph[src]:

                if neighbor not in visited:

                    new_distance = distances[src] + graph[src][neighbor]

                    if new_distance < distances.get(neighbor, float('inf')):
                        distances[neighbor] = new_distance

                        predecessors[neighbor] = src

            # mark as visited
            visited.append(src)

            # now that all neighbors have been visited: recurse

            # select the non visited node with lowest distance 'x'

            # run Dijskstra with src='x'

            unvisited = {}

            for k in graph:

                if k not in visited:
                    unvisited[k] = distances.get(k, float('inf'))

            x = min(unvisited, key=unvisited.get)

            dijkstra(graph, x, dest, visited, distances, predecessors)

    if __name__ == "__main__":
        dijkstra({'Laidlaw South': {'CCF Hut': 45, 'Astroturf': 100, 'Mount Olympus': 135},

                  'Mount Olympus': {'Laidlaw South': 135, 'Dining Hall': 85},

                  'Swimming Pool': {'CCF Hut': 40},

                  'CCF Hut': {'Swimming Pool': 40, 'Laidlaw South': 45, 'Chalmers East': 45},

                  'Astroturf': {'Laidlaw South': 100, 'The Arena': 80},

                  'The Arena': {'Astroturf': 80, 'Sports Hall': 30},

                  'Sports Hall': {'The Arena': 30, 'Napier': 50},

                  'Dining Hall': {'Mount Olympus': 85, 'Chalmers East': 60, 'Chalmers West': 90, 'Main Entrance': 50},

                  'Mappa Mundi': {'Chalmers East': 80, 'Napier': 10},

                  'Napier': {'Mappa Mundi': 10, 'Music': 40, 'Sports Hall': 50},

                  'Music': {'Napier': 40, 'Computing': 15},

                  'Computing': {'Music': 15, 'Art': 20},

                  'Art': {'Computing': 20, 'Gibson': 40},

                  'Gibson': {'Art': 40, 'Chalmers West': 35},

                  'Chalmers West': {'Gibson': 35, 'Chalmers East': 80, 'Dining Hall': 90},

                  'Chalmers East': {'Chalmers West': 80, 'Dining Hall': 60, 'Mappa Mundi': 80, 'CCF Hut': 45},

                  'Main Entrance': {'Dining Hall': 50, 'Pringle Centre': 135},

                  'Pringle Centre': {'Main Entrance': 135, 'Rifle Range': 50, 'Tennis Courts': 50},

                  'Rifle Range': {'Pringle Centre': 50, 'Pringle Staff Housing': 30, 'Pringle House': 20},

                  'Tennis Courts': {'Pringle Centre': 50},

                  'Pringle Staff Housing': {'Rifle Range': 50, 'Secret Garden': 10},

                  'Pringle Football Pitch': {'Pringle Centre': 30},

                  'Pringle House': {'Rifle Range': 20, 'Pringle Football Pitch': 30, 'Secret Garden': 40},

                  'Secret Garden': {'Pringle House': 40, 'Pringle Staff Housing': 10, 'The Stable': 60},

                  'The Stable': {'Secret Garden': 60, 'School Entrance': 75},

                  'School Entrance': {'The Stable': 75}

                  }, 'Laidlaw South', 'School Entrance')


def result(request):
    return render(request, 'saved.html')

def saved(request):
    return render(request, 'result.html')