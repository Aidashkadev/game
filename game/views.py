from django.shortcuts import render, redirect, get_object_or_404
from .models import Cat

# READ — список котов
def cat_list(request):
    cats = Cat.objects.all()
    return render(request, 'game/cats.html', {'cats': cats})

# CREATE — создать кота
def create_cat(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Cat.objects.create(name=name)
        return redirect('cat_list')
    return render(request, 'game/create_cat.html')

# UPDATE — редактировать кота
def edit_cat(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    if request.method == 'POST':
        cat.name = request.POST.get('name')
        cat.level = request.POST.get('level')
        cat.mood = request.POST.get('mood')
        cat.save()
        return redirect('cat_list')
    return render(request, 'game/edit_cat.html', {'cat': cat})

# DELETE — удалить кота
def delete_cat(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    cat.delete()
    return redirect('cat_list')

def index(request):
    cats = Cat.objects.all()
    return render(request, 'game/index.html', {'cats': cats})
