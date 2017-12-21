from django.contrib import admin

# Register your models here.
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
