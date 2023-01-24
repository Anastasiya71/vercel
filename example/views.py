from django.shortcuts import render
from .models import RandomNumber


def index(request):
    num = RandomNumber.objects.all().first()
    return render(request, 'index.html', context={"num": num})
