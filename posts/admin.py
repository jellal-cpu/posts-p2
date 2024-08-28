from django.contrib import admin 
from posts.models import Posts 


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['id', 'title']
    list_filter = ['created_at',]

