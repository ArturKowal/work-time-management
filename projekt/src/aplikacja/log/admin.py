from django.contrib import admin

from .models import Log

class SignInAdmin(admin.ModelAdmin):
    list_display = ['who','what','when_in']
    ordering = ['when_in']

admin.site.register(Log,SignInAdmin)