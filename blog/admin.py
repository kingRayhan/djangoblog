from django.contrib import admin
from .models import Blog, Category
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    list_display = ('id', 'title', 'is_published',
                    'category', 'author', 'created_at')
    list_display_links = ('id', 'title')
    list_editable = ('is_published', 'category')
    search_fields = ('title', 'category__title')
    list_filter = ('is_published', 'category', 'created_at')
    date_hierarchy = 'created_at'
    prepopulated_fields = {"slug": ("title",)}
    ordering = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
