from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, "index.html")

def decision(request):
      if not request.user.is_authenticated:
          return render(request, "login.html", {"message": None})
      context = {
          "user": request.user
      }
      return HttpResponseRedirect(reverse("order"))

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("decision"))
    else:
        return render(request, "login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})

def sign_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        cpassword= request.POST["cpassword"]
        if not password == cpassword:
            return render(request, "sign_up.html", {"message": "Passwords do not match."})
        try:
            new_user = User.objects.create_user(username, None, password)
        except:
            return render(request, "sign_up.html", {"message": "Username Already Taken."})
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse("decision"))
    return render(request, "sign_up.html", {"message": None})

def order(request):
    return render(request, "order.html")

def order_form(request):
    return render(request, "order.html")
