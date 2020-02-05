from django.contrib import admin

from .models import SignIn , SignOut

class SignInAdmin(admin.ModelAdmin):
    list_display = ['who','when_in']
    ordering = ['when_in']
#	pass
class SignOutAdmin(admin.ModelAdmin):
    list_display = ['who','when_out']
    ordering = ['when_out']
#	pass
admin.site.register(SignIn,SignInAdmin)
admin.site.register(SignOut,SignOutAdmin)

#admin.site.register(SignIn)