from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

class AccountAdmin(UserAdmin):
	list_display = ('first_name','last_name','email','ident','date_joined','last_login')
	search_fields = ( 'first_name','last_name','email','ident')
	ordering = ('last_name','first_name')
	readonly_fields= ('date_joined','last_login')
	filter_horizontal=()
	list_filter = ()
	fieldsets = ()

	def has_add_permission(self, request, obj=None):
		return False

admin.site.register(Account,AccountAdmin)