from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from library.models import *
import pandas as pd


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user1 = guest(username=username, password=password, email=email)
        user1.save()
        return render(request, 'sign.html')
    return render(request, template_name='registration.html')


def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user2 = authenticate(request, username=username, password=password)
        if user2 is not None:
            login(request, user2)
            request.session['username'] = username
            return render(request, 'Booking.html')
    else:
        return render(request, 'sign.html')


def book(request):
    if request.method == 'POST':
        check = request.POST['check']
        checkout = request.POST['checkout']
        type1 = request.POST['type']
        username = request.session['username']
        book1 = booking(name=username, check=check, checkout=checkout, type=type1)
        book1.save()
    return redirect("/booking/")


def payment(request):
    username = request.session['username']
    y = booking.objects.filter(name=username)

    for x in y:
        if x.type == 'single':
            a = x.check
            b = x.checkout
            z = b - a
            c = z * 100
            td = pd.Timedelta(c)
        elif x.type == 'double':
            a = x.check
            b = x.checkout
            z = b - a
            c = z * 200
            td = pd.Timedelta(c)
        return render(request, "Payment.html", {'guest': td.days})
    return render(request, "Payment.html", {'guest': 0})


def cancel(request):
    username = request.session['username']
    r = booking.objects.filter(name=username).delete()
    return redirect("/booking/")


def logout_request(request):
    logout(request)
    request.session.clear()
    return redirect("/booking/")


class AboutView(TemplateView):
    template_name = "booking.html"


class AboutView2(TemplateView):
    template_name = "about.html"


class AboutView4(TemplateView):
    template_name = "sign.html"


class AboutView6(TemplateView):
    template_name = "rooms.html"


class AboutView7(TemplateView):
    template_name = "services.html"
