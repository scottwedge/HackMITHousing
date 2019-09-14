from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required

attempt = False

def index(request):
    # simply redirecting to the first page
    return render(request, 'login.html', {'attempt': attempt})

def check(request):
    # login authetication
    id = request.POST['id']
    pw = request.POST['pw']

    user = authenticate(username=id, password=pw)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('login:main'))
    else:
        return render(request, 'login.html', {'attempt': True})


@login_required(login_url='/login')
def main(request):
    if request.user.profile.type == 1:
        return render(request, 'employer.html')
    elif request.user.profile.type == 2:
        return render(request, 'employee.html')


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:index'))
