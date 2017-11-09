from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.staticfiles import *




def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user     = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request.user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')

def loggedin(request):
    return render_to_response('loggedin.html', {'full_name': request.user.username})

def invalid(request):
    return render_to_response('invalid.html')


def logout(request):
    auth.logout(request)
    return render_to_response('index.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')

    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    print args
    return render_to_response('registration.html', args)


def register_success(request):
    return render_to_response('index.html')


