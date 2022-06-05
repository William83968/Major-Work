from django.shortcuts import redirect, render
from .models import Item, Category, House
from .forms import CategoryForm, HouseForm, ItemForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def list_items_all(request, category_id):
    category_list = Category.objects.all()
    all_houses = House.objects.all()
    item_list = Item.objects.filter(category__id=category_id)
    return render(request, 'list_items_all.html', {
        'category_list':category_list,
        'category_id':int(category_id),
        'all_houses':all_houses,
        'item_list':item_list
    })

def list_items_h(request, house_id, category_id):
    category_list = Category.objects.filter(house__id=house_id) 
    all_houses = House.objects.all()
    item_list = Item.objects.filter(category__id=category_id)
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
    item_list = Item.objects.all()
    return render(request, 'list_categories.html', {
        'category_list':category_list,
        'all_houses':all_houses,
        'house_id':int(house_id),
        'item_list':item_list
    })

def items(request):
    category_list = Category.objects.all()
    item_list = Item.objects.all()
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
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_item?submitted=True')
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
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('items')
    return render(request, 'update_item.html', {
        'item':item,
        'form':form
    })

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect('items')


def categories(request):
    category_list = Category.objects.all()
    submitted = False
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/categories?submitted=True')
        return render(request, 'categorys.html', {
            'category_list':category_list,
            'form':form
        })
    else:
        form = CategoryForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'categorys.html', {
            'category_list':category_list,
            'form':form,
            'submitted':submitted
        })

def update_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('categories')
    return render(request, 'update_category.html', {
        'category':category,
        'form':form
    })

def delete_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()
    return redirect('categories')

def add_house(request):
    submitted = False
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_house?submitted=True')
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

