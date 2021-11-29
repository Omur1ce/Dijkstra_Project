from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
import sys
import json
from urllib.request import urlopen
import urllib
from .models import Locations
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def about(request):
    return HttpResponse(
        '<h1> Bad website.... </h1>''<h2> Additionally, chee chee wanted to be on the website so here is here shoutout </h2>')


def dijkstra_page(request):
    response = HttpResponse("hellooo")
    response.set_cookie('graph', {'laidlawS': {'swimming': 100, 'astro': 100, 'mount': 135},
                                  'mount': {'laidlawS': 135, 'dining': 85},
                                  'swimming': {'laidlawS': 100},
                                  'astro': {'laidlawS': 100},
                                  'dining': {'mount': 85}
                                  })
    return response


def dijkstra_cookie(request):
    return render(request, 'Dijkstra.html')


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
    return render(request, 'test.html')


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


def dijkstra(request, graph, src, dest, visited=[], distances={}, predecessors={}):
    src = request.COOKIES.get('src')
    dest = request.COOKIES.get('dest')
    graph = request.COOKIES.get('graph')

    # a few error prevention checks
    if request.COOKIES.get('src') not in graph:
        raise TypeError('The Source is not in the graph')
    if request.COOKIES.get('dest') not in graph:
        raise TypeError('The destination is not in the graph')
        # ending condition
    if request.COOKIES.get('src') == request.COOKIES.get('dest'):
        # We build the shortest path and display it
        path = []
        pred = request.COOKIES.get('dest')
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
        # reverses the array
        readable = path[0]
        for i in range(1, len(path)): readable = path[i] + ' ---> ' + readable
        time = distances[request.COOKIES.get('dest')] // 1.4
        # prints it
        print('shortest path: ' + str(path))
        print("Directions: " + readable)
        print("Distance: " + str(distances[request.COOKIES.get('dest')]) + 'm')
        print('Estimated time: ' + str(time) + 's')
    else:
        # if it is the initial  run, initializes the cost
        if not visited:
            distances[request.COOKIES.get('src')] = 0
        # visit the neighbors
        for neighbor in graph[request.COOKIES.get('src')]:
            if neighbor not in visited:
                new_distance = distances[request.COOKIES.get('src')] + graph[request.COOKIES.get('src')][neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = request.COOKIES.get('src')
        # mark as visited
        visited.append(request.COOKIES.get('src'))
        # now that all neighbors have been visited: recurse
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))
        x = min(unvisited, key=unvisited.get)
        dijkstra(graph, src,dest , visited, distances, predecessors)

    if __name__ == "__main__":
        src = request.COOKIES.get('src')
        dest = request.COOKIES.get('dest')
        graph = request.COOKIES.get('graph')
        dijkstra(graph, src, dest)

# """<html><script>window.location.replace('/');</script></html>"""
# dijkstra(graph,x,dest,visited,distances,predecessors)
