from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "timestamp", "updated"]
    class Meta:
        model = User

admin.site.register(User, UserAdmin)
