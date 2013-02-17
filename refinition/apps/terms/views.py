from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from django.utils.timezone import utc
from datetime import *
from terms.models import *
from terms.forms import *


def home(request):
    """ """
    versions       = Version.objects.all()
    latest_version = versions[0]
    return render_to_response('home.html',{ 'versions': versions, 'version': latest_version }, context_instance=RequestContext(request))
    
    
def version_view(request):
    pass
    
    
def version_save(request, html):
    """ """
    term = Term.objects.get(title='doubt')
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    slug = slugify(now)
    version = Version(term=term, slug=slug, html=html)
    version.save()
    
    versions = Version.objects.all()
    
    return render_to_response('home.html', 
       {
           'versions' : versions,
           'version'  : version
       }, context_instance=RequestContext(request))            


def version_load(request, version_slug=None):
   """ """
   version  = get_object_or_404(Version, slug=version_slug)
   print version
   versions = Version.objects.all()

   return render_to_response('home.html', 
      {
          'versions' : versions,
          'version'  : version
      }, context_instance=RequestContext(request))
