"""defining url patterns for etergrams application"""
from django.conf.urls import url
from . import views

urlpatterns = [
    #home page
    url(r'^$', views.index, name='index'),

    #show all tags
    url(r'^tags/', views.tags, name='tags'),
    
]
