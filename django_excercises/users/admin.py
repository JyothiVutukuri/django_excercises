from django.contrib import admin
from django_excercises.users.models import Profile
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from django.contrib.auth import get_user_model
User = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fields = [
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "is_active",
        "password",
    ]
    fieldsets = []
    list_filter = []
    readonly_fields = ["username"]
    list_display = ["id", "email", "get_full_name", "is_staff", "is_superuser", "is_active"]
    search_fields = ["email", "first_name", "last_name"]

    inlines = [ProfileInline, ]



