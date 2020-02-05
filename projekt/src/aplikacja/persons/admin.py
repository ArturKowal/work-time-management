from django.contrib import admin

from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'position']
    ordering = ['last_name','first_name']

admin.site.register(Person,PersonAdmin)