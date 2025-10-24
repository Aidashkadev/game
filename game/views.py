from django.shortcuts import render, redirect, get_object_or_404
from .models import Cat
from .forms import CatForm

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
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
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
    cat.score += 1  # каждый клик добавляет очки
    if cat.score % 10 == 0:  # например, каждые 10 очков кот получает уровень
        cat.level += 1
        cat.milk += 5
    cat.save()
    return redirect('index_with_cat', cat_id=cat.id)

def rating(request):
    cats = Cat.objects.all().order_by('-score')
    return render(request, 'game/rating.html', {'cats': cats})

def index_with_cat(request, cat_id):
    cats = Cat.objects.all()
    cat = get_object_or_404(Cat, id=cat_id)
    return render(request, 'game/index.html', {'cats': cats, 'cat': cat})