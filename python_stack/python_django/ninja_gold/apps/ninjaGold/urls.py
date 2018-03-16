from django.conf.urls import url
import views
urlpatterns=[
    url(r'^$', views.index),
    url(r'^process_money/(?P<name>\w+)', views.process),
    url(r'^clear$', views.clear)
]
