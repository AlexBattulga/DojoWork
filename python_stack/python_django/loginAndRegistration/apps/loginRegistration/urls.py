from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/registration$', views.process),
    url(r'^users/login$', views.login)
]
