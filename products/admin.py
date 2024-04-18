from django.contrib import admin
from .models import Products, Category
@admin.register(Products)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'price',  'body']
    ordering = ['status', 'publish_time']

@admin.register(Category)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
