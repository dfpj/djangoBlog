from django.contrib import admin
from .models import Article
# Register your models here.

class AricleAdmin(admin.ModelAdmin):
    list_display=('title','slug','jpublish','status')
    list_filter=('publish','status')
    search_fields=('title','desc')
    prepopulated_fields={'slug':('title',)}
    ordering=['status','-publish']

admin.site.register(Article,AricleAdmin)
