from django.urls import path

from . import views

app_name = 'employee'

urlpatterns = [
    path('', views.index, name='index'),
    # path('add_apply', views.add_apply, name='add_apply'),
    # path('view_match', views.view_match, name='view_match'),
    # path('accept', views.accept, name='accept'),
    # path('reject', views.reject, name='reject'),
    # path('rate_er', views.rate_er, name='rate_er')
]
