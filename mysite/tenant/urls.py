from django.urls import path

from . import views

app_name = 'tenant'

urlpatterns = [
    path('', views.index, name='index'),
    # path('rent_house', views.rent_house, name='rent_house'),
    # path('view_landlord', views.view_landlord, name='view_landlord')
]
