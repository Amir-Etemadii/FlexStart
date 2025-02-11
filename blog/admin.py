from django.contrib import admin
from .models import Post, Category


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    get_production_date = Post.get_production_date
    list_display = ('id', 'title', 'author', get_production_date)
    list_display_links = ('id', 'title')
    search_fields = ('id',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
