from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Category, Note


admin.site.register(Author, UserAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "color")


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("text", "category", "author")
