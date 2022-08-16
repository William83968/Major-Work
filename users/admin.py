from django.contrib import admin
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import User
from .forms import UserRegisterForm

class UserAdmin(AuthUserAdmin):
    add_form = UserRegisterForm
    update_form_class = UserChangeForm

admin.site.register(Profile)
