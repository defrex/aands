
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import RSVPForm

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


