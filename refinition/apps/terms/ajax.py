from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from terms.views import *


@dajaxice_register(method='POST')
def version_load(request, version_slug=None):
    """ """
    return version_load(request, version_slug)


@dajaxice_register(method='POST')
def version_save(request, data):
    """ """
    return version_save(request, deserialize_form(data))