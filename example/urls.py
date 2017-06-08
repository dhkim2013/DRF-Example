from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stuffs/$', views.StuffList.as_view()),
    url(r'^stuffs/(?P<pk>[0-9]+)/$', views.StuffDetail.as_view()),
]
