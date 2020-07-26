from django.conf.urls import url
from django.urls import path
import app_user.views

urlpatterns = [
    path(r'', app_user.views.AppUserAPI.as_view()),
]