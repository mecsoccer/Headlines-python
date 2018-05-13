from django.conf.urls import url
from . import views

app_name = 'news'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sources/$', views.sources_list, name='list_sources'),
    url(r'^countries/$', views.countries_list, name='list_countries'),
    url(r'^sources/(?P<source>[a-z-]+)/$', views.source_news, name='sources'),
    url(r'^countries/(?P<country>[a-z]+)/$', views.country_news, name='countries')
]
