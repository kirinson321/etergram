"""defining url patterns for etergrams application"""
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #home page
    url(r'^$', views.index, name='index'),

    #page with all tags
    url(r'^tags/$', views.tags, name='tags'),

    #page with all entries for a specific tag
    url(r'^tags/(?P<tag_id>\d+)/$', views.tag, name='tag'),

    #page for adding a new tag
    url(r'^new_tag/$', views.new_tag, name='new_tag'),

    #page for adding new entries
    #deprecated, dependent on a single tag, should not have created this
    #url(r'^new_entry/(?P<tag_id>\d+)/$', views.new_entry, name='new_entry'),

    #current page for adding new entries
    url(r'^new_entry/$', views.new_entry, name='new_entry'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
