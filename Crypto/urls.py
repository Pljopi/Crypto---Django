from django.urls import path
from . import views

app_name = 'Crypto'

urlpatterns = [

    path('list/', views.get_list, name='list'),
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),

]
