from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm


def register(request):

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(
                "accounts:login"
            )

    else:
        form = RegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


def user_login(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                messages.success(
                    request,
                    "Login successful!"
                )

                return redirect(
                    "students:student-list"
                )

            else:

                form.add_error(
                    None,
                    "Invalid username or password."
                )

    else:

        form = LoginForm()

    return render(
        request,
        "accounts/login.html",
        {"form": form}
    )


def user_logout(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out."
    )

    return redirect(
        "accounts:login"
    ) 