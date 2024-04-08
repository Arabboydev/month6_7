from django.contrib import admin
from .models import Book, Author, BookingBook, Comments
from import_export.admin import ImportExportModelAdmin

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("id", "first_name", "last_name", "birth_date")
    search_fields =("id", "last_name", "first_name")

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ("id", "title", "description_20", "price", "count", "author", "comments_count", "create_date")
    list_display_links = ("id", "title", "description_20", "price", "count", "author", "comments_count", "create_date")
    search_fields = ("id", "title")
    ordering = ("title", "author")
    autocomplete_fields = ("author", )

    def description_20(self, obj):
        return obj.description[:5]

    def comments_count(self, obj):
        return obj.comments.all().count()

@admin.register(BookingBook)
class BookingBookAdmin(ImportExportModelAdmin):
    list_display = ("id", "take_date", "returned_date")

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "student")

