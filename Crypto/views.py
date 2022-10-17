from django.http import HttpResponse
from django.utils import timezone
import datetime
import requests
from django.template import loader
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.template import RequestContext

now = datetime.datetime.now()


def homepage(request):
    return render(request=request, template_name='Crypto/home.html')


def get_price_raw(request, cripto_currency, currency):
    response = requests.get(
        "https://api.coinbase.com/v2/prices/%s-%s/spot" % (cripto_currency, currency)).json()
    return response


def get_list_raw(request):
    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/supported_vs_currencies').json()
    return response


def get_list(request):
    response = get_list_raw(request)
    template = loader.get_template('Crypto/list.html')
    context = {
        'response': response,
    }
    return HttpResponse(template.render(context, request))


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
                return redirect("Crypto/homepage", RequestContext(request))
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="Crypto/login.html", context={"login_form": form})
