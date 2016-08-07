from django.conf.urls import url
from . import views

app_name = 'music' #name-spacing the urls!

urlpatterns = [
    #/music/
    url(r'^$', views.index, name = 'index'),
    #/music/id e.g. /music/180
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail')

]
