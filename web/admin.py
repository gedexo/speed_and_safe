from django.contrib import admin

from .models import *

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message')
    search_fields = ('name', 'email', 'phone', 'subject')
    list_filter = ('name', 'email')
    ordering = ('-id',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)
    prepopulated_fields = {'slug': ('title',)}