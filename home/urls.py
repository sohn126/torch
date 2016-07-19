from django.conf.urls import patterns, url

from home import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^tables/$', views.tables, name='tables'),
    url(r'^forms/$', views.forms, name='forms'),
    url(r'^forgot_password/$', views.forgot_password, name='forgot_password'),
    url(r'^visual/$', views.visual, name='visual'),
    url(r'^d3test/$', views.d3test, name='d3'),
]
