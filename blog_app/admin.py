from django.contrib import admin
from .models import*

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    class Meta:
        model = Blog

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
