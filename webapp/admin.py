from django.contrib import admin
from .models import*

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

    class Meta:
        model = Project

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)