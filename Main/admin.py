from django.contrib import admin
from .models import Item, User, Category, House

# Register your models here.
admin.site.register(Item)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(House)

