from django.contrib import admin
from .models import Post_the_blog
# Register your models here.


@admin.register(Post_the_blog)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']