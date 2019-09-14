from django.urls import path

from . import views

app_name = 'landlord'

urlpatterns = [
    path('', views.index, name='index'),
    # path('add_house', views.add_house, name='add_house'),
    # path('view_candidate', views.view_candidate, name='view_candidate')
]
