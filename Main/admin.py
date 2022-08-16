from django.contrib import admin
from django import forms
from .models import Item, User, Category, House
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import User


class MyUserCreationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    class Meta(UserCreationForm.Meta):
        model = User


class UserAdmin(AuthUserAdmin):
    add_form = MyUserCreationForm
    update_form_class = UserChangeForm


# Register your models here.
admin.site.register(Item)
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(House)

