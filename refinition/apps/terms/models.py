from django.conf import settings
from django.db.models import *
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.template import loader, Context
from django.core.urlresolvers import reverse
from django.template import Template
from tinymce.models import HTMLField


class Base(Model):
    """
    Base model for all of the models.
    """
    class Meta:
        abstract = True
                    
    created     = DateTimeField(auto_now_add=True, editable=False)
    updated     = DateTimeField(auto_now=True, editable=False)
    is_active   = BooleanField(default=1)        
        
    def __unicode__ (self):
        if hasattr(self, "title") and self.title:
            return self.title
        else:
            return "%s" % (type(self))


class Term(Base):
    """
    """    
    class Meta:
        ordering = ['created']

    title       = CharField(max_length=50, null=False)
    slug        = SlugField(max_length=120, null=False)
                

class Version(Base):
    """
    """    
    class Meta:
        ordering = ['-created']
    
    term        = ForeignKey(Term, default="doubt")
    slug        = SlugField(max_length=120)
    html        = HTMLField(null=False)
    

import signals