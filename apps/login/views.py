from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils import simplejson
from login.forms import LoginForm
from login.utils import render_login

def handle_login(request):
    if not request.method == 'POST':
        return HttpResponse('fail')
    resp = dict()
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            resp['status'] = 'LOGGED_IN'
        else:
            if len(User.objects.filter(username=username)) > 0:
                resp['status'] = 'BAD_PASS'
            else:
                user = User.objects.create_user(username, '', password)
                user_authed = authenticate(username=username, password=password)
                login(request, user_authed)
                resp['status'] = 'NEW_USER'
    else:
        resp['status'] = 'FORM_ERROR'
        form_errors = dict()
        for key, val in form.errors.items():
            form_errors[key] = str(val.as_text())
        resp['errors'] = form_errors
    return HttpResponse(simplejson.dumps(resp))

def login_form(request):
    return HttpResponse(render_login(request))
