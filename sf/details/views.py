from django.shortcuts import render, redirect, HttpResponse
from .models import Contect
# Create your views here.


def index(request):
    if request.method == "POST":
        user = request.POST.get('user', '')
        name = request.POST.get('name', '')
        sem = request.POST.get('sem', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        image = request.POST.get('image', '')
        if user and name and sem and email:
         contect=Contect(user=user,name=name,sem=sem,phone=phone,email=email, image=image)
        contect.save()

    return render(request, 'index.html')