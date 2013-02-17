from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from dajaxice.core import dajaxice_autodiscover, dajaxice_config


admin.autodiscover()
dajaxice_autodiscover()

# direct browser requests to the different apps
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),    
)

urlpatterns += patterns('',
    url(r'^', include('terms.urls')),
)

# static files url patterns
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }),
   )