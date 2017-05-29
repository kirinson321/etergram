"""defining url patterns for etergrams application"""
from django.conf.urls import url
from . import views


urlpatterns = [
    #home page
    url(r'^$', views.index, name='index'),

    #page with all tags
    url(r'^tags/$', views.tags, name='tags'),

    #page with all entries for a specific tag
    url(r'^tags/(?P<tag_id>\d+)/$', views.tag, name='tag'),

    #page for adding a new tag
    url(r'^new_tag/$', views.new_tag, name='new_tag'),

]
