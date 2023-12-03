from django.template.defaulttags import url
from django.urls import path

from .views import post_list, post_detail, post_new

urlpatterns = [
    path('', post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
    url(r'^post/new/$', post_new, name='post_new'),
]
