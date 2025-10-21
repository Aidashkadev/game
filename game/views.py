from django.shortcuts import render, redirect, get_object_or_404
from .models import Cat
from .forms import CatForm

def index(request):
    return render(request, 'game/index.html')

def cat_list(request):
    cats = Cat.objects.all()
    return render(request, 'game/cat_list.html', {'cats': cats})

def create_cat(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
    else:
        form = CatForm()
    return render(request, 'game/create_cat.html', {'form': form})

def edit_cat(request, cat_id):
    cat = get_object_or_404(Cat, pk=cat_id)
    if request.method == 'POST':
        form = CatForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
    else:
        form = CatForm(instance=cat)
    return render(request, 'game/edit_cat.html', {'form': form})

def delete_cat(request, cat_id):
    cat = get_object_or_404(Cat, pk=cat_id)
    if request.method == 'POST':
        cat.delete()
        return redirect('cat_list')
    return render(request, 'game/delete_cat.html', {'cat': cat})
