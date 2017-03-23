from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

from . import client


class NoReCaptchaWidget(forms.widgets.Widget):
    g_nocaptcha_response = 'g-recaptcha-response'
    template = getattr(settings, "NORECAPTCHA_WIDGET_TEMPLATE",
                       'nocaptcha_recaptcha/widget_nocaptcha.html')

    def __init__(self, site_key=None,
                 gtag_attrs=None, js_params=None, *args, **kwargs):
        self.site_key = site_key if site_key else \
            settings.NORECAPTCHA_SITE_KEY
        super(NoReCaptchaWidget, self).__init__(*args, **kwargs)
        self.gtag_attrs = gtag_attrs or {}
        self.js_params = js_params or {}

    def render(self, name, value, gtag_attrs=None, **kwargs):
        return mark_safe(u'%s' % client.displayhtml(
            self.template, self.site_key, self.gtag_attrs, self.js_params))

    def value_from_datadict(self, data, files, name):
        return data.get(self.g_nocaptcha_response, None)


class InvisibleReCaptchaWidget(NoReCaptchaWidget):
    template = getattr(settings, "INVISIBLE_RECAPTCHA_WIDGET_TEMPLATE",
                       'nocaptcha_recaptcha/widget_invisible.html')
