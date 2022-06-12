from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('items', views.items, name="items"),
    path('list_categories/<house_id>', views.list_categories, name="list_categories"),
    path('categories', views.categories, name="categories"),
    path('list_items_all/<category_id>', views.list_items_all, name="list_items_all"),
    path('list_items_h/<house_id>/<category_id>', views.list_items_h, name="list_items_h"),
    path('categories', views.categories, name="categories"),
    path('category/<category_id>', views.category, name="category"),
    path('search_items', views.search_items, name="search_items"),
    path('item/<item_id>', views.item, name="item"),
    path('update_category/<category_id>', views.update_category, name="update_category"),
    path('update_item/<item_id>', views.update_item, name="update_item"),
    path('add_item', views.add_item, name="add_item"),
    path('delete_item/<item_id>', views.delete_item, name="delete_item"),
    path('delete_category/<category_id>', views.delete_category, name="delete_category"),
    path('add_house', views.add_house, name="add_house"),
    path('list_house', views.list_house, name="list_house"),
    path('update_house/<house_id>', views.update_house, name="update_house"),
    path('delete_house/<house_id>', views.delete_house, name="delete_house"),
]