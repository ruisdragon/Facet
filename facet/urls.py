from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'facet.blog.views.index'),
    url(r'^notepad/$', 'facet.blog.views.notepad'),
    url(r'^notepad/(?P<pk_id>\d+)/$', 'facet.blog.views.detail'),
    url(r'^blog/$', 'facet.blog.views.blog'),
    url(r'^blog/(?P<pk_id>\d+)/$', 'facet.blog.views.detail'),
    url(r'^about/$', 'facet.blog.views.about'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
