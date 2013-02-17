from django.forms import *
from django.forms.formsets import BaseFormSet
from django.utils.translation import ugettext as _
from terms.models import *


class VersionForm (ModelForm):
    class Meta:
        model = Version