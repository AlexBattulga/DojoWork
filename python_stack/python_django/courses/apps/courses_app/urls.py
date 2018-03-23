from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^course/decision/(?P<id>\d+)$', views.decision),
    url(r'^course/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^course/add$', views.add)
]
