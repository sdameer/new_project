from django.shortcuts import render
from django.http import HttpResponse
from .lang import *

def home(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input')
        new_data = main_func(user_input)
        return render(request, "output.html", {"new_data": new_data})

    return render(request, "home.html")
