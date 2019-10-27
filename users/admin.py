from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import Files

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(CustomUser, CustomUserAdmin)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('description', 'email', 'created_at')
    def email(self, instance):
        return instance.user.email

admin.site.register(Files, FilesAdmin)
