"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import include, path, reverse

def redirect(request):
    return HttpResponseRedirect(reverse('login:main'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect),
    path('login/', include('login.urls')),
    path('employee/', include('employee.urls')),
    path('employer/', include('employer.urls')),
    path('landlord/', include('landlord.urls')),
    path('tenant/', include('tenant.urls'))
    # yet to be implemented:
    # - upload images of the house;
    # - images of employers & employees
    # - background check
]
