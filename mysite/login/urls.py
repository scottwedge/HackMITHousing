from django.urls import path

from . import views
from django.urls import path

# app_name = 'login'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('your-identity/', views.get_name, name='main'),
    path('logout_view', views.logout_view, name='logout')
]
