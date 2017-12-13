__author__ = 'achachar'
from django.conf.urls import url
from . import views

app_name = 'main_app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add_contact/?$', views.add_contact, name='add_contact')
]
