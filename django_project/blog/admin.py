from django.contrib import admin
from .models import Post,Category
# Register your models here.



class PostInline(admin.StackedInline):
    model = Post



class CategoryAdmin(admin.ModelAdmin):
    inlines=[PostInline]


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title','content','slug']
    list_filter = ['draft','created_at']
    list_display = ['title','author','category','created_at','draft','rating']
    list_editable = ['author','category','draft','rating']
    

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)