from django.template.loader import get_template
from django.template import RequestContext
from login.forms import LoginForm

def render_login(request):
    template = get_template('login.html')
    form = LoginForm()
    return template.render(RequestContext(request, {'form':form}))
