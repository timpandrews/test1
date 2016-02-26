from django.contrib import admin

# Register your models here.
from .forms import User_Registartion_Form
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "timestamp", "updated"]
    form = User_Registartion_Form

admin.site.register(User, UserAdmin)
