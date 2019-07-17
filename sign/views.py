from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            # return HttpResponse("login success")
            respone = HttpResponseRedirect("/event_manger/")
            # respone.set_cookie('user', username, 3600)
            request.session['user'] = username
            return respone
        else:
            return render(request, 'index.html', {'error': 'username or password errors!'})

@login_required()
def event_manger(request):
    # username = request.COOKIES.get('user', '')
    username = request.session.get('user', '')
    print('username:' + username)
    return render(request, 'event_manger.html', {'user': username})
