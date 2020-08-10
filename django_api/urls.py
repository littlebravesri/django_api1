"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import analysis.views
from . import views

from app_user.views import AppUserAPI

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'items', views.ItemListViewSet)
router.register(r'modelless', views.ExampleModelLessView, basename='modelless')
router.register(r'analysis/modellessapi', analysis.views.ModelLessAPI, basename='analysismlapi')
router.register(r'analysis/modelbasedapi', analysis.views.ModelBasedAPI, basename='analysismbapi')
router.register(r'app_user', AppUserAPI, basename='appuser')

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login', views.login),
    path('logout', views.logout),
    path('check_auth', views.check_auth),
    #    path('post_list', views.post_list, name='post_list'),

    path('analysis/', include('analysis.urls')),
    path('app_user/', include('app_user.urls')),

)


