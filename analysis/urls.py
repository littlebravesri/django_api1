from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from analysis.views import *


router = routers.DefaultRouter()
router.register(r'modellessapi', ModelLessAPI, basename="modellessapi")
router.register(r'modelbasedapi', ModelBasedAPI, basename="modelbasedapi")

mlapi = ModelLessAPI.as_view({'post': 'create'})
mbapi = ModelBasedAPI.as_view({'post': 'create'})

urlpatterns = [
    path(r'', include(router.urls)),
    url(r'^modelbasedapi/(?P<id>\d+)/$', ModelBasedAPI_ID.as_view(), name='mbapiid'),
]

#
# urlpatterns = [
#     #path(r'', include(router.urls)),
#     path(r'modellessapi/', ModelLessAPI.as_view()),
#     path(r'modelbasedapi/', ModelBasedAPI.as_view()),
#     url(r'^modelbasedapi/(?P<id>\d+)/$', ModelBasedAPI_ID.as_view(), name='mbapi'),
# ]

