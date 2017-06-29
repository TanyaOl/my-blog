from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
list_display = ['title', 'category', 'likes', 'dislikes', 'slug', 'image', 'image_img', 'timestamp', 'autor']
readonly_fields = ['image_img',]
fields = ['category', 'title', 'slug', 'metakey', 'metadesc', 'text_redactor', 'text_redactor_full', 'tag', 'timestamp', 'autor', 'image', 'image_img', 'body', 'likes', 'dislikes']
#class ImageAdmin(admin.ModelAdmin):
 #   list_display = ('title','imgfile','image_img', )
 #admin.site.register(Image,ImageAdmin)
