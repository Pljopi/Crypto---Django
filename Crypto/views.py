from django.http import HttpResponse
import datetime
import requests
from django.template import loader
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
import Crypto.views_favorites as fav
import Crypto.views_get as get

now = datetime.datetime.now()


def favorite(request):
    return render(request, "Crypto/favorite.html", {})


def dashboard(request):
    return render(request, "Crypto/dashboard.html", {})


def homepage(request, *args, **kwargs):
    return render(request, "Crypto/home.html", {})


def navbar(request):
    return render(request, "Crypto/navbar.html", {})


def get_price(request):
    response = get.get_list_raw(request)
    template = loader.get_template('Crypto/get-price.html')
    context = {
        'response': response,
    }
    return HttpResponse(template.render(context, request))


def display_price(request):
    if request.method == 'POST':
        cripto_currency = request.POST.get('crypto_currency')
        currency = request.POST.get('currency')
        response = get.get_price_raw(request, cripto_currency, currency)
        template = loader.get_template('Crypto/display-price.html')
        context = {
            'price': response['data']['amount'],
            'crypto_currency': cripto_currency,
            'currency': currency,
        }
        return HttpResponse(template.render(context, request))

    return redirect("Crypto:get-price")


def get_list(request):
    response = get.get_list_raw(request)
    template = loader.get_template('Crypto/list.html')
    context = {
        'response': response,
    }
    return HttpResponse(template.render(context, request))


def add_favorite(request):
    if request.method == 'POST':
        tags = request.POST.get('favorite')
        fav.favorites_insert_tag(tags)
    return redirect("Crypto:list")


def list_favorite(request):
    response = fav.favorites_list()
    template = loader.get_template('Crypto/favorite.html')
    context = {
        'response': response,
    }
    return HttpResponse(template.render(context, request))


def remove_favorite(request):
    if request.method == 'POST':
        tags = request.POST.get('favorite')
        fav.favorites_remove_tag(tags)
    return redirect("Crypto:favorite")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("Crypto:homepage")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="Crypto/register.html",
                  context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/home", RequestContext(request))
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="Crypto/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("Crypto:homepage")
