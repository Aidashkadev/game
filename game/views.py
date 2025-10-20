from django.shortcuts import render
from .models import Cat

def index(request):
    cats = Cat.objects.all()
    return render(request, 'game/index.html', {'cats': cats})
