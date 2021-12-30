from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render


def home_page(request: HttpRequest):
    return render(request, "home/index.html")
