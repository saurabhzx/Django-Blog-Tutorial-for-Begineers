from django.conf.urls import patterns, url
from blogging import views

urlpatterns = patterns('',
    url(r'^$', 'blogging.views.index', name='index')
)