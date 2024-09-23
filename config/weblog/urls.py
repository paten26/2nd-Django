from django.urls import path

from config.weblog.views import homepage

urlpatterns = [
    path('', homepage)
]
