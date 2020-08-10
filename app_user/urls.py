from django.urls import path
from app_user.views import  *

"""
Registering 'app_user app's urls 
"""
AppUser = AppUserAPI.as_view({'post': 'create'})

urlpatterns = [
    path(r'', AppUser),
]