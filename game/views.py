from django.shortcuts import render, redirect, get_object_or_404
from .models import Cat
from .forms import CatForm
from django.http import JsonResponse


def index(request, cat_id=None):
    cats = Cat.objects.all()
    cat = None
    if cat_id:
        cat = get_object_or_404(Cat, id=cat_id)
    return render(request, 'game/index.html', {'cats': cats, 'cat': cat})

def cat_list(request):
    cats = Cat.objects.all()
    return render(request, 'game/cat_list.html', {'cats': cats})

def create_cat(request):
    if request.method == 'POST':
        form = CatForm(request.POST, request.FILES)  # важно: request.FILES для фото
        if form.is_valid():
            form.save()
            return redirect('cat_list')  # или куда хочешь
    else:
        form = CatForm()
    return render(request, 'game/create_cat.html', {'form': form})

def edit_cat(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    if request.method == 'POST':
        form = CatForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
    else:
        form = CatForm(instance=cat)
    return render(request, 'game/edit_cat.html', {'form': form, 'cat': cat})

def delete_cat(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    if request.method == 'POST':
        cat.delete()
        return redirect('cat_list')
    return render(request, 'game/delete_cat.html', {'cat': cat})

def play_cat(request, cat_id):
    # просто страница игры/клика — показывает кота и кнопку клика
    cat = get_object_or_404(Cat, id=cat_id)
    return render(request, 'game/play_cat.html', {'cat': cat})

def click_cat(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    # Увеличиваем очки
    cat.score = (cat.score or 0) + 1
    # Если достигли кратного 20 — даём молоко
    if cat.score % 100 == 0:
        cat.milk = (cat.milk or 0) + 1
    cat.save()
    return JsonResponse({'score': cat.score, 'milk': cat.milk})


def rating(request):
    cats = Cat.objects.all().order_by('-score')
    return render(request, 'game/rating.html', {'cats': cats})

def index_with_cat(request, cat_id):
    cats = Cat.objects.all()
    cat = get_object_or_404(Cat, id=cat_id)
    return render(request, 'game/index.html', {'cats': cats, 'cat': cat})