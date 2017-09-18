from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^new/$', views.new),
    url(r'^create/$', views.create),
    url(r'^(\d+)/$', views.show),
    url(r'^(\d+)/edit/$', views.edit),
    url(r'^(\d+)/delete/$', views.destroy)
    ]