from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/register$', views.register),
    url(r'^user/login$', views.login),
    url(r'^home_page$', views.home),
    url(r'^add/book$', views.add_book),
    url(r'^add_new/book$', views.process_new_book),
    url(r'^clear_session$', views.clear),
    url(r'^show/book/details/(?P<book_id>\d+)$', views.book_details),
    url(r'^destroy/(?P<book_id>\d+)', views.destroy_reviews),
    url(r'^add_review/(?P<book_id>\d+)$', views.add_review),
    url(r'^user/details/(?P<user_id>\d+)$', views.user_details)
]
