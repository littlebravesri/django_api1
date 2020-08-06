from django.conf.urls import url
from django.urls import path
from rest_framework import routers

import analysis.views

# router = routers.DefaultRouter()
# router.register(r'analysis/', analysis.views.ModelLessAPI)
# router.register(r'modelbasedapi/', analysis.views.ModelBasedAPI)
router = routers.DefaultRouter()
#router.register(r'', views.VocabViewSet, 'vocabs')
#router.register(r'modellessapi/', views.TermViewSet, 'terms')
#router.register(r'modelbasedapi/', views.DisciplineViewSet, 'disciplines')

urlpatterns = [
    #path(r'', analysis.views.analysisAPI),
    path(r'modellessapi/', analysis.views.ModelLessAPI.as_view()),
    path(r'modelbasedapi/', analysis.views.ModelBasedAPI.as_view()),
    url(r'^modelbasedapi/(?P<id>\d+)/$', analysis.views.ModelBasedAPI_ID.as_view(), name='mbapi'),
]

