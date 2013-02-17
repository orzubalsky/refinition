from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from terms.views import *


@dajaxice_register(method='POST')
def load_version(request, version_slug=None):
    """ """
    return version_load(request, version_slug)


@dajaxice_register(method='POST')
def save_version(request, html):
    """ """
    return version_save(request, html)