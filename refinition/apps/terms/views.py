from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from terms.models import *
from terms.forms import *


def home(request):
    """ """
    versions       = Version.objects.all()
    latest_version = versions[0]
    return render_to_response('home.html',{ 'versions': versions, 'latest_version': latest_version }, context_instance=RequestContext(request))
    
def version_view(request):
    pass