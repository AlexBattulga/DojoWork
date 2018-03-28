from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^signin$', views.signin, name='sign_in'),
    url(r'^register$', views.register, name='register'),
    url(r'^register_process$', views.process_register),
    url(r'^signin_process$', views.process_signin),
    url(r'^display_dash$', views.display_dash),
    url(r'^create$', views.create),
    url(r'^create_process$', views.process_create),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^edit_users/(?P<id>\d+)$', views.process_edit),
    url(r'^edit_password/(?P<id>\d+)$', views.process_password),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^profile/(?P<id>\d+)$', views.profile),
    url(r'^message_process/(?P<id>\d+)$', views.process_message)
]
