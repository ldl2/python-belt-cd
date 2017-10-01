from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^main$', views.index, name="test_main"),
    url(r'^register$', views.register, name="test_register"),
    url(r'^login$', views.login, name="test_loginr"),
    url(r'^dashboard$', views.dashboard, name="test_dashboard"),
    url(r'^logout$', views.logout, name="test_logout"),
    url(r'^wish_list/create$', views.create, name="test_create"),
    url(r'^wish_list/new$', views.new, name="test_new"),
    url(r'^wish_items/(?P<id>\d+)$', views.item, name='test_item'),
    url(r'^wish_items/(?P<id>\d+)/like$', views.like),
    url(r'^wish_items/(?P<id>\d+)/unlike$', views.unlike),
    url(r'^wish_items/(?P<id>\d+)/delete$', views.remove)
]
