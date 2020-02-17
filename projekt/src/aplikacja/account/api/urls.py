from django.urls import path
from account.api.views import api_detail_who_view 


app_name = 'Who_are_you'

urlpatterns = [
	path('<ident>/',api_detail_who_view,name="detail"),

]
