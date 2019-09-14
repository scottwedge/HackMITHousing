import json
from xml.etree import ElementTree

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#
# @login_required(login_url='/login')
# def index(request):
#     return HttpResponseRedirect(reverse("employee:add_apply"))


# Create your views here.
