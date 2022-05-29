from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('items', views.items, name="items"),
    path('list_categories/<house_id>', views.list_categories, name="list_categories"),
    path('categories', views.categories, name="categories"),
    path('list_items_all/<category_id>', views.list_items_all, name="list_items_all"),
    path('list_items_h/<house_id>/<category_id>', views.list_items_h, name="list_items_h"),
    path('categories', views.categories, name="categories"),
    path('search_items')
]