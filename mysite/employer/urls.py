from django.urls import path

from . import views

app_name = 'employer'

urlpatterns = [
    path('', views.index, name='index'),
    # path('add_work', views.add_work, name='add_work'),
    # path('view_match', views.view_match, name='view_match'),
    # path('accept', views.accept, name='accept'),
    # path('reject', views.reject, name='reject'),
    # path('rate_ee', views.rate_ee, name='rate_ee')
]
