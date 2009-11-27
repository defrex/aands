
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import RSVPForm

def main(request):
    if request.method == 'POST':
        f = RSVPForm(request.POST)
        if f.is_valid():
            f.save()
            return render_to_response('rsvp/thanks.html', 
                    context_instance=RequestContext(request))
    else:
        f = RSVPForm()
    return render_to_response('rsvp/main.html', {'form': f},
            context_instance=RequestContext(request))


