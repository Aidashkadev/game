from django.shortcuts import render, redirect
from .models import Cat
from .forms import CatForm

# READ — список котов
def cat_list(request):
    cats = Cat.objects.all()
    return render(request, 'game/cats.html', {'cats': cats})

# CREATE — создать кота

def create_cat(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CatForm()
    return render(request, 'game/create_cat.html', {'form': form})

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
    cat_id = request.GET.get('cat_id')
    cat = None
    if cat_id:
        from .models import Cat
        cat = Cat.objects.filter(id=cat_id).first()
    return render(request, 'game/index.html', {'cat': cat})
