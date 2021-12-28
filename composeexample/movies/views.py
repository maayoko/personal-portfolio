from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    print(request.path)
    return HttpResponse("Hello Django")


def get_movies(request: HttpRequest):
    return render(request, "movies_list.html")
