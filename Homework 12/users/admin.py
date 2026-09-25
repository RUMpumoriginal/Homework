from django.contrib import admin

from users.models import UserCreate


@admin.register(UserCreate)
class UserCreate(admin.ModelAdmin):
    list_display = ("name", "birth_date")
    list_filter = ("isAdmin",)
    search_fields = ("name",)