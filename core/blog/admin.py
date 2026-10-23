from django.contrib import admin
from blog.models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):

    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    #fields
    #exclude
    list_display = ['title', 'id', 'author', 'status', 'published_date', 'updated_date']
    list_filter = ['author', 'status']
    search_fields = ['title', 'content']
    ordering = ['created_date']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
