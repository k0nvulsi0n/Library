from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Author, AuthorAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'status')
    list_filter = ('author', 'status')
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'genre', 'summary')
        }),
        ('Personal data', {
            'fields': ('status', 'date_read')
        }),
    )


admin.site.register(Book, BookAdmin)

