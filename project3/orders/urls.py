from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("decision", views.decision, name="decision"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.sign_up, name="sign_up"),
    path("order", views.order, name="order"),
    path("orderform", views.order_form, name="order_form")
]
