from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Category

# Create a category form
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'house')
        labels={
            'name':'Category Name',
            'house':'House Name',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder':'Category Name'}),
            'house':  forms.Select(attrs={'class':'form-select w-75', 'placeholder':'House Name'}),
        }
