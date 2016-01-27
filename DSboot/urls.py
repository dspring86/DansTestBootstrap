from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?i)DSbootTab/$', views.boot_list, name='boot_list'),
]