from django import forms
from .models import MyBook

class MyBookForm(forms.ModelForm):
    class Meta:
        model = MyBook
        fields = ['title', 'author', 'price', 'stock', 'genre']
