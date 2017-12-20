__author__ = 'achachar'
from django.conf.urls import url
from . import views
from django.views.static import serve
from django.conf import settings

app_name = 'main_app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add_contact/?$', views.add_contact, name='add_contact')
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    ]
