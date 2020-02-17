from django.urls import path
from log.api.views import api_create_log_view


app_name = 'Logs'

urlpatterns = [
	path('create',api_create_log_view,name="create"),

]
