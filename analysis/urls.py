from django.conf.urls import url
from django.urls import path
from . import views
from . import models

from django.urls import path, re_path
from django.contrib import admin
import analysis.views

urlpatterns = [
    #path('', admin.site.urls),
    path(r'', analysis.views.Analysis.as_view()),
    # re_path(r'(?P<pk>\d+)', analysis.views.TypeView.as_view()),
    url(r'', views.index, name='index'),
]

