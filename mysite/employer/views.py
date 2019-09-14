from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# @login_required(login_url='/login')
# def index(request):
#     return HttpResponseRedirect(reverse("employer:add_work"))
