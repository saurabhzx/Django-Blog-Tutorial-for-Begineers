from django.conf.urls import patterns, url, include

from blogging.api import *
from blogging import views

urlpatterns = patterns('',
    #url(r'^$', 'blogging.views.index', name='index')
)

user_urls = patterns('',
   url(r'^$', AuthorList.as_view(), name='Author-list'),
    url(r'^/(?P<id>[0-9]+)$', AuthorDetail.as_view(), name='Author-detail'),
    url(r'^/(?P<id>[0-9]+)/posts$', AuthorPost.as_view(), name='AuthorPost-list'),
    (r'^$', PostList.as_view()),
    url(r'^/(?P<user__pk>[0-9]+)$', PostDetail.as_view(), name='Post-detail'),
)

urlpatterns += user_urls


 