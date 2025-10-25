from django import forms
from .models import Cat

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'description', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border rounded-lg p-2'}),
            'description': forms.Textarea(attrs={'class': 'w-full border rounded-lg p-2'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'w-full border rounded-lg p-2'}),
        }
