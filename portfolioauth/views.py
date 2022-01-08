from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.http.request import HttpRequest

from .login_form import LoginForm
from .register_form import RegisterForm
from .models import User

# Create your views here.


def check_passwords(password1, password2):
    return password1 == password2


def login(request: HttpRequest):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            try:
                user: User = User.objects.get(
                    username=request.POST["username"])
                password_matches = check_passwords(
                    user.password, request.POST["password"])

                if password_matches:
                    return HttpResponseRedirect("/dashboard")
            except User.DoesNotExist:
                errors = "Wrong email or password"

        errors = errors if isinstance(errors, str) else form.errors
        return render(request, "login/index.html", {"errors": errors})

    elif request.method == "GET":
        return render(request, "login/index.html")

    else:
        return HttpResponseBadRequest()


def register(request: HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            User.objects.create(
                username=request.POST["username"],
                full_name=request.POST["full_name"],
                password=request.POST["password"],
                email=request.POST["email"],
                phone=request.POST["phone"])
            return HttpResponseRedirect("/dashboard")

        return render(request, "register/index.html", {"errors": form.errors})

    elif request.method == "GET":
        return render(request, "register/index.html")

    else:
        return HttpResponseBadRequest()
