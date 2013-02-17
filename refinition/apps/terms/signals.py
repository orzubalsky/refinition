from terms.models import *
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# adding 'dispatch_uid' because this signal was getting reigstered twice. 'dispatch_uid' just needs to be some unique string.
#
# more info here on a better way to fix this problem:
# http://stackoverflow.com/questions/2345400/why-is-post-save-being-raised-twice-during-the-save-of-a-django-model
@receiver(post_save, sender=Version, dispatch_uid="refinition.apps.terms.signals")
def version_save_callback(sender, instance, **kwargs):
    """ """    
    pass