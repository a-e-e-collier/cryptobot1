from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name = 'settings'),
    path('startbot', views.startbot, name = 'startbot'),

]
