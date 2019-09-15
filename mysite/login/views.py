from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import IdentityForm

def index(request):
    # simply redirecting to the first page
    return render(request, 'login.html')

def get_name(request):
    if request.method == 'POST':
        form = IdentityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['identity'])
            if form.cleaned_data['your_identity'] == 'employer':
                return render(request, "employer.html")
            if form.cleaned_data['your_identity' == 'employee']:
                return render(request, "employee.html")
        else:
            print("got to form invalid")
            return HttpResponseRedirect('/login')


def login(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:index'))
