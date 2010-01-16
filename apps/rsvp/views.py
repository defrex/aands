
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import RSVPForm
from models import RSVP

def main(request):
    if request.method == 'POST':
        fs = RSVPForm(request.POST)
        if fs.is_valid():
            fs.save()
            f = RSVPForm()
            thanks = True
        else:
            f = fs
            thanks = False
    else:
        f = RSVPForm()
        thanks = False
    return render_to_response('rsvp/main.html', {'form': f, 'thanks': thanks},
            context_instance=RequestContext(request))

def browse(request):
    rsvps = RSVP.objects.all()
    
    rsvps = rsvps.order_by(request.GET.get('sort', 'attending'))
    
    if request.GET.get('attending') == 'false':
        rsvps = rsvps.filter(attending=False)
    
    if request.GET.get('not_attending') == 'false':
        rsvps = rsvps.filter(attending=True)
    
    return render_to_response('rsvp/browse.html', {'rsvps': rsvps},
            context_instance=RequestContext(request))

