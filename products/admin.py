from django.contrib import admin

# Register your models here.

from .models import Product ,Caregory,Tag ,Review

class ReviewInline(admin.TabularInline):
    model = Review

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("name", "category", "price",)


admin.site.register(Product, ProductAdmin)

admin.site.register(Caregory)
admin.site.register(Tag)