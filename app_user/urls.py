from django.urls import path
from app_user.views import  *

AppUser = AppUserAPI.as_view({'post': 'create'})

urlpatterns = [
    path(r'', AppUser),
]