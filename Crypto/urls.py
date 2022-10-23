from django.urls import path

from Crypto import views_get
from . import views
from Crypto.views_get import get_list_raw

app_name = 'Crypto'

urlpatterns = [
    path('add/', views.add_favorite, name='add'),
    path('remove', views.remove_favorite, name='remove'),
    path('get-price', views.get_price, name='get-price'),
    path('display-price', views.display_price, name='display-price'),
    path('list/', views.get_list, name='list'),
    path('favorite/', views.list_favorite, name='favorite'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("", views.homepage, name="homepage"),
    path("home", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("navbar", views.navbar, name="navbar"),
]
