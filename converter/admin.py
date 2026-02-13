from django.contrib import admin
from .models import Category, Topic

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_pro', 'created_at')
    list_filter = ('category', 'is_pro')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
