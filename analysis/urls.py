from django.conf.urls import url
from django.urls import path
import analysis.views

urlpatterns = [
    path(r'modellessapi', analysis.views.ModelLessAPI.as_view()),
    path(r'modelbasedapi', analysis.views.ModelBasedAPI.as_view()),
    url(r'^modelbasedapi/(?P<id>\d+)/$', analysis.views.ModelBasedAPI_ID.as_view(), name='mbapi'),
]

