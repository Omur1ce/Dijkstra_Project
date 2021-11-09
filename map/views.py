from django.shortcuts import render
from django.http import HttpResponse
import sys
import json
from urllib.request import urlopen
import urllib
from .models import MyModel


def home(request):
    return render(request, 'home.html')


def about(request):
    return HttpResponse(
        '<h1> Bad website.... </h1>''<h2> Additionally, chee chee wanted to be on the website so here is here shoutout </h2>')


def collect(request):
    url = "http://127.0.0.1:8000/"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return HttpResponse(data)


def saveCriteria(request):
    if request.method == "POST":
        context = {}
        title = request.POST.get('quantity')
        print(title)
    return render(request, "test.html", context)


def test(request):
    return render(request, 'test.html')


def save_values(request):
    src = request.GET['dropdown1']
    dest = request.GET['dropdown2']

    return render(request, 'home.html')


def dijkstra(request, graph, src, dest, visited=[], distances={}, predecessors={}):
    request.session[src] = 'LadlawS'
    request.session[dest] = 'dining'
    request.session[graph] = {'laidlawS': {'swimming': 100, 'astro': 100, 'mount': 135},
                              'mount': {'laidlawS': 135, 'dining': 85},
                              'swimming': {'laidlawS': 100},
                              'astro': {'laidlawS': 100},
                              'dining': {'mount': 85}
                              }

    # a few error prevention checks
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')
        # ending condition
    if src == dest:
        # We build the shortest path and display it
        path = []
        pred = dest
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
        # reverses the array
        readable = path[0]
        for i in range(1, len(path)): readable = path[i] + ' ---> ' + readable
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
    graph = {'laidlawS': {'swimming': 100, 'astro': 100, 'mount': 135},
             'mount': {'laidlawS': 135, 'dining': 85},
             'swimming': {'laidlawS': 100},
             'astro': {'laidlawS': 100},
             'dining': {'mount': 85}
             }
    src = 'laidlawS'
    dest = 'dining'

    dijkstra(graph, src, dest)

# """<html><script>window.location.replace('/');</script></html>"""
# dijkstra(graph,x,dest,visited,distances,predecessors)
