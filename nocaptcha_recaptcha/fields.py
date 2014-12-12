import os
import sys

from django import forms
from django.conf import settings

try:
    from django.utils.encoding import smart_unicode
except ImportError:
    from django.utils.encoding import smart_text as smart_unicode

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from . import client
from .widgets import NoReCaptchaWidget


class NoReCaptchaField(forms.CharField):
    default_error_messages = {
        'captcha_invalid': _('Incorrect, please try again.')
    }

    def __init__(self, site_key=None, secret_key=None,
                 gtag_attrs={}, js_params={}, *args, **kwargs):
        """
        site_key = the Google provided site_key
        secret_key = the Google provided secret_key
        gtag_attrs = html input attributes to provide
            to the g-recaptcha tag
        js_params = parameters to passed to the javascript backend

        See: https://developers.google.com/recaptcha/docs/display
        """
        site_key = site_key if site_key else \
            settings.NORECAPTCHA_SITE_KEY
        self.secret_key = secret_key if secret_key else \
            settings.NORECAPTCHA_SECRET_KEY

        self.widget = NoReCaptchaWidget(
            site_key=site_key, gtag_attrs=gtag_attrs, js_params=js_params)
        self.required = True
        super(NoReCaptchaField, self).__init__(*args, **kwargs)

    def get_remote_ip(self):
        """
        Return the remote IP from the request.
        First check the REMOTE_ADDR header and then the
        HTTP_X_FORWARDED_FOR header.
        """
        f = sys._getframe()
        while f:
            if 'request' in f.f_locals:
                request = f.f_locals['request']
                if request:
                    remote_ip = request.META.get('REMOTE_ADDR', '')
                    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
                    ip = remote_ip if not forwarded_ip else forwarded_ip
                    return ip
            f = f.f_back

    def clean(self, value):
        super(NoReCaptchaField, self).clean(value)
        g_nocaptcha_response_value = smart_unicode(value)
        if os.environ.get('NORECAPTCHA_TESTING', None) == 'True' \
                and g_nocaptcha_response_value == 'PASSED':
            return value

        check_captcha = client.submit(
            g_nocaptcha_response_value, secret_key=self.secret_key,
            remoteip=self.get_remote_ip())

        if not check_captcha.is_valid:
            raise ValidationError(self.error_messages['captcha_invalid'])
        return value
