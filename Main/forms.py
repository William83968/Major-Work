from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Category, Item, House

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

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'category', 'cost', 'placement', 'expiry_date', 'account', 'sold_price')
        labels={
            'name': 'Item Name',
            'category':'Item Category',
            'cost':'Item Cost',
            'placement':'Item Location',
            'expiry_date':'Expiry Date',
            'account':'Account',
            'sold_price':'Sold Price',
        }
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control w-75'}),
            'category':  forms.Select(attrs={'class':'form-select w-75', 'placeholder':''}),
            'cost':  forms.NumberInput(attrs={'class':'form-control w-75'}),
            'placement':  forms.TextInput(attrs={'class':'form-control w-75'}),
            'expiry_date':  forms.DateInput(attrs={'class':'form-control w-75', 'type':'date'}),
            'account':  forms.URLInput(attrs={'class':'form-control w-75'}),
            'sold_price':  forms.NumberInput(attrs={'class':'form-control w-75'}),
        }

class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = ('name', 'owner', 'state', 'suburb', 'street', 'unit_number')
        labels = {
            'name': 'House Name',
            'owner': 'House Owner',
            'state': 'State Address',
            'suburb': 'Suburb Address',
            'street': 'Street Address',
            'unit_number': 'Unit Number',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control w-75'}),
            'owner': forms.Select(attrs={'class': 'form-select w-75'}),
            'state': forms.TextInput(attrs={'class': 'form-control w-75'}),
            'suburb': forms.TextInput(attrs={'class': 'form-control w-75'}),
            'street': forms.TextInput(attrs={'class': 'form-control w-75'}),
            'unit_number': forms.TextInput(attrs={'class': 'form-control w-75'}),
        }
