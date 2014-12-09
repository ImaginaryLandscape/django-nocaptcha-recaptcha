from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

from . import client


class NoReCaptchaWidget(forms.widgets.Widget):
    g_nocaptcha_response = 'g-recaptcha-response'

    def __init__(self, site_key=None,
                 gtag_attrs={}, js_params={}, *args, **kwargs):
        self.site_key = site_key if site_key else \
            settings.NORECAPTCHA_SITE_KEY
        super(NoReCaptchaWidget, self).__init__(*args, **kwargs)
        self.gtag_attrs = gtag_attrs
        self.js_params = js_params

    def render(self, name, value, gtag_attrs=None, **kwargs):
        return mark_safe(u'%s' % client.displayhtml(
            self.site_key, self.gtag_attrs, self.js_params))

    def value_from_datadict(self, data, files, name):
        return data.get(self.g_nocaptcha_response, None)
