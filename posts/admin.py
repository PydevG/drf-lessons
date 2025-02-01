from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display =  ["title", "created"]
    list_filter = ['created']
    
admin.site.register(Post, PostAdmin)