from django.urls import path

from .views import LogView

app_name = "log"

urlpatterns = [
    path('logs/', LogView.as_view()),
]
