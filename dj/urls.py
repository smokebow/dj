from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import views
from django.views.generic import TemplateView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj.views.home', name='home'),
    # url(r'^dj/', include('dj.foo.urls')),
    url(r'^$', TemplateView.as_view (template_name='index.html')),
    url(r'^base2$', TemplateView.as_view (template_name='base2.html')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
