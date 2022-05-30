from django.shortcuts import redirect, render
from .models import Item, Category, House
from .forms import CategoryForm
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

def categories(request):
    category_list = Category.objects.all()
    submitted = False
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_category?submitted=True')
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

def update_category(request, item_id):
    category = Category.objects.get(pk=item_id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('categories')
    return render(request, 'update_category.html', {
        'category':category,
        'form':form
    })