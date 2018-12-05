from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^create_verify/$', views.create_verify, name='create_verify'),
    url(r'^update_user/(?P<id>\d+)/$', views.update_user, name='update_user'),
    url(r'^show/(?P<id>\d+)/$', views.show, name='show'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
]
