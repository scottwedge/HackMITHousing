from django.urls import path

from . import views
from django.urls import include, path, reverse

app_name = 'login'

urlpatterns = [
    path('', views.index, name='index'),
    path('check', views.check, name='check'),
    path('first', views.main, name='main'),
    path('logout_view', views.logout_view, name='logout')
]
