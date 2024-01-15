from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    def get_queryset(self, request):
        return super().get_queryset(request).using("mongo")


admin.site.register(Product, ProductAdmin)
