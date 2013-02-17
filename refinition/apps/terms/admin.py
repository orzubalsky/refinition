from django.utils.safestring import mark_safe
from terms.models import *
from django.contrib import admin

class BaseAdmin(admin.ModelAdmin):
    """ Base admin model."""
    pass

# register admin models
admin.site.register(Term)
admin.site.register(Version)