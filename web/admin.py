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

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('title',)

@admin.register(ProductEnquiry)
class ProductEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'product', 'quantity', 'message')
    search_fields = ('name', 'email', 'phone', 'product')
    list_filter = ('name', 'email', 'product')
    ordering = ('-id',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('title',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass