from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['id', 'author', 'pub_date', 'title', 'content']
    readonly_fields = ('id',)