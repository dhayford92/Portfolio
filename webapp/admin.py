from django.contrib import admin
from .models import*

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

    class Meta:
        model = Project



class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')

    class Meta:
        model = Contact



admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
admin.site.register(AddProfileImage)