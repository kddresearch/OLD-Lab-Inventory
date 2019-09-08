from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.

# acts as app entry
def home(request):
    return render(request, 'inventory/home.html', {})

def logout_view(request):
    logout(request)
    return redirect('/')
    # Redirect to a success page.

def login(request):
    if request.POST:
        if 'login' in request.POST:
            return HttpResponseRedirect('/youloggedin/')
        else:
            return HttpResponseRedirect('/youregistered')
    else:
        return render(request, 'inventory/login.html')


def login(request):
    if request.POST:
        if 'login' in request.POST:
            return HttpResponseRedirect('/youloggedin/')
        else:
            return HttpResponseRedirect('/youregistered')
    else:
        return render(request, 'inventory/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'inventory/register.html', {'form': form})
