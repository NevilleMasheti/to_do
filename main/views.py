# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from main.models import Event

def home(request):
    if request.method == "POST":
        pass
    return render_to_response("create.html", {}, context_instance=RequestContext(request))
