from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

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
    
@admin.register(ProductCategory)
class ProductCategoryAdmin(ImportExportModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('title',)

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('title', 'category',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('title', 'category',)
    list_editable = ('category',)

@admin.register(ProductEnquiry)
class ProductEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'product', 'quantity', 'message')
    search_fields = ('name', 'email', 'phone', 'product')
    list_filter = ('name', 'email', 'product')
    ordering = ('-id',)

@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('title',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass

@admin.register(Meta)
class MetaAdmin(admin.ModelAdmin):
    list_display = ("page", "meta_title",)