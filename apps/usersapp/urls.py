from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.users),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^new/$', views.register)
    ]