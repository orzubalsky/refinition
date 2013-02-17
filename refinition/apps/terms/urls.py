from django.conf.urls import patterns, include, url

urlpatterns = patterns('terms.views',
    url(r'^version/(?P<version_slug>[-\w]+)$', 'version_view', name='version-view'),
    url(r'^$', 'home', name='home'),
)



