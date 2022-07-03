from django.contrib import admin

# Register your models here.
from django.contrib import admin
from guestbook.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created_at', 'status']
    list_display_links = ['author']
    list_filter = ['author']
    search_fields = ['author', 'content']
    fields = ['author', 'email', 'content', 'created_at', 'updated_at', 'status']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Book, BookAdmin)
