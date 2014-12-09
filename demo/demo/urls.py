from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from . import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', views.DemoView.as_view(template_name="index.html"), {}, name="index"),
    url(r'^success/$', TemplateView.as_view(template_name="success.html"), {}, name="success"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
