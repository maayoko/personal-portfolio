from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.http.request import HttpRequest

from .login_form import LoginForm
from .register_form import RegisterForm

# Create your views here.


def login(request: HttpRequest):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect("/dashboard")

        return render(request, "login/index.html", {"errors": form.errors})

    elif request.method == "GET":
        return render(request, "login/index.html")

    else:
        return HttpResponseBadRequest()


def register(request: HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect("/dashboard")

        return render(request, "register/index.html", {"errors": form.errors})

    elif request.method == "GET":
        return render(request, "register/index.html")

    else:
        return HttpResponseBadRequest()
