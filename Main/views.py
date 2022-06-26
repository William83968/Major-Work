# Import Django core packages
from django.shortcuts import redirect, render
from .models import Item, Category, House
from .forms import CategoryForm, HouseForm, ItemForm
from django.http import HttpResponseRedirect
from django.contrib import messages

#Import Calendar Stuff
import calendar
from calendar import HTMLCalendar
from datetime import datetime
import pytz

# Import Pagination Stuff
from django.core.paginator import Paginator


# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    # Initialise the user
    name = "Mr.X"
    if request.user != "AnonymousUser":
        name = request.user

    # Get the time
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    timezone = pytz.timezone("Australia/Sydney")
    
    # Format the time
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now(pytz.timezone('Australia/Sydney'))
    current_year = now.year
    time = now.strftime('%I:%M:%S %p ')

    # Item near Expiry
    items = Item.objects.all()


    # Get the number of each model
    item_count = Item.objects.all().count()
    category_count = Category.objects.all().count()
    house_count = House.objects.all().count()

    return render(request, "home.html", 
                    {'name':name, 
                    'year':year, 
                    'month':month, 
                    "cal":cal, 
                    'current_year':current_year,
                    'time':time,
                    'item_count':item_count,
                    'category_count':category_count,
                    'house_count':house_count,
                    'items':items})

def list_items_all(request, category_id):
    category_list = Category.objects.all()
    all_houses = House.objects.all()
    item_list = Item.objects.filter(category__id=category_id).order_by('name')
    return render(request, 'list_items_all.html', {
        'category_list':category_list,
        'category_id':int(category_id),
        'all_houses':all_houses,
        'item_list':item_list
    })

def list_items_h(request, house_id, category_id):
    category_list = Category.objects.filter(house__id=house_id) 
    all_houses = House.objects.all()
    item_list = Item.objects.filter(category__id=category_id).order_by('name')
    return render(request, 'list_items_h.html', {
        'category_list':category_list,
        'category_id':int(category_id),
        'house_id':int(house_id),
        'all_houses':all_houses,
        'item_list':item_list
    })

def list_categories(request, house_id):
    category_list = Category.objects.filter(house__id=house_id)
    all_houses = House.objects.all()
    item_list = Item.objects.filter(category__house__id=house_id).order_by('name')
    return render(request, 'list_categories.html', {
        'category_list':category_list,
        'all_houses':all_houses,
        'house_id':int(house_id),
        'item_list':item_list
    })

def items(request):
    category_list = Category.objects.all()
    item_list = Item.objects.all().order_by('name')
    house_list = House.objects.all()
    return render(request, 'items.html', {
        'category_list':category_list,
        'house_list':house_list,
        'item_list':item_list
    })

def search_items(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        items = Item.objects.filter(name__contains=searched)
        return render(request, 'search_items.html', {
            'searched':searched,
            'items':items
        })
    else:
        return render(request, 'search_items.html', {})

def item(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'item.html', {
        'item':item
    })

def add_item(request):
    submitted = False
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ("Item added successfully"))
            return HttpResponseRedirect('/main/add_item?submitted=True')
    else:
        form = ItemForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_item.html', {
        'form':form,
        'submitted':submitted
    })

def update_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, ("Item updated successfully"))
        return redirect('items')
    return render(request, 'update_item.html', {
        'item':item,
        'form':form
    })

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    messages.success(request, ("Item deleted successfully"))
    return redirect('items')


def categories(request):
    category_list = Category.objects.all()
    # Set up pagination
    p = Paginator(category_list, 3)
    page = request.GET.get('page')
    categories = p.get_page(page)
    nums = 'a' * categories.paginator.num_pages

    submitted = False
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Category added successfully"))
            return HttpResponseRedirect('/main/categories?submitted=True')
        return render(request, 'categories.html', {
            'category_list':category_list,
            'categories':categories,
            'form':form,
            'nums':nums
        })
    else:
        form = CategoryForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'categories.html', {
            'category_list':category_list,
            'form':form,
            'categories':categories,
            'submitted':submitted,
            'nums':nums
        })

def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    item_list = Item.objects.filter(category__id=category_id)
    item_count = item_list.count()
    return render(request, "category.html", {
        'category':category,
        'item_list':item_list,
        'item_count':item_count
    })

def update_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        messages.success(request, ("Category updated successfully"))
        return redirect('categories')
    return render(request, 'update_category.html', {
        'category':category,
        'form':form
    })

def delete_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()
    messages.success(request, ("Category deleted successfully"))
    return redirect('categories')

def add_house(request):
    submitted = False
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("House added successfully"))
            return HttpResponseRedirect('/main/add_house?submitted=True')
    else:
        form = HouseForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_house.html', {
        'form':form,
        'submitted':submitted
    })

def list_house(request):
    all_houses = House.objects.all()
    return render(request, 'list_house.html', {
        'all_houses':all_houses
    })

def update_house(request, house_id):
    house = House.objects.get(pk=house_id)
    form = HouseForm(request.POST or None, instance=house)
    if form.is_valid():
        form.save()
        messages.success(request, ("House updated successfully"))
        return redirect('list_house')
    return render(request, 'update_house.html', {
        'house':house,
        'form':form
    })

def delete_house(request, house_id):
    house = House.objects.get(pk=house_id)
    house.delete()
    messages.success(request, ("House deleted successfully"))
    return redirect('list_house')


