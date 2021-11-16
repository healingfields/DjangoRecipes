from django.contrib import admin

# Register your models here.
from .models import Article

class AdminArticle(admin.ModelAdmin):

    list_display = ['id','title']
    search_fields = ['title','content']

admin.site.register(Article,AdminArticle)