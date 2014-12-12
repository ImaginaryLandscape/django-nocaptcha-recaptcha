import logging

import django

if django.VERSION[1] >= 5:
    import json
else:
    from django.utils import simplejson as json

from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import get_language
from django.utils.encoding import force_text

from ._compat import want_bytes, urlencode, Request, urlopen, PY2

logger = logging.getLogger(__name__)

DEFAULT_VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
DEFAULT_FALLBACK_URL = "https://www.google.com/recaptcha/api/fallback"
DEFAULT_WIDGET_TEMPLATE = 'nocaptcha_recaptcha/widget.html'

VERIFY_URL = getattr(settings, "NORECAPTCHA_VERIFY_URL",
                     DEFAULT_VERIFY_URL)

FALLBACK_URL = getattr(settings, "NORECAPTCHA_FALLBACK_URL",
                       DEFAULT_FALLBACK_URL)

WIDGET_TEMPLATE = getattr(settings, "NORECAPTCHA_WIDGET_TEMPLATE",
                          DEFAULT_WIDGET_TEMPLATE)


class RecaptchaResponse(object):
    def __init__(self, is_valid, error_codes=None):
        self.is_valid = is_valid
        self.error_codes = error_codes


def displayhtml(site_key, gtag_attrs, js_params):
    """Gets the HTML to display for reCAPTCHA

    site_key -- The public api key provided by Google ReCaptcha
    """

    if 'hl' not in js_params:
        js_params['hl'] = get_language()[:2]

    return render_to_string(
        WIDGET_TEMPLATE,
        {
            'fallback_url': FALLBACK_URL,
            'site_key': site_key,
            'js_params': js_params,
            'gtag_attrs': gtag_attrs,
        })


def submit(g_nocaptcha_response_value, secret_key, remoteip):
    """
    Submits a reCAPTCHA request for verification. Returns RecaptchaResponse
    for the request

    recaptcha_response_field -- The value of recaptcha_response_field
    from the form
    secret_key -- your reCAPTCHA private key
    remoteip -- the user's ip address
    """

    if not (g_nocaptcha_response_value and len(g_nocaptcha_response_value)):
        return RecaptchaResponse(
            is_valid=False,
            error_codes=['incorrect-captcha-sol']
        )

    params = urlencode({
        'secret': want_bytes(secret_key),
        'remoteip': want_bytes(remoteip),
        'response': want_bytes(g_nocaptcha_response_value),
    })

    if not PY2:
        params = params.encode('utf-8')

    req = Request(
        url=VERIFY_URL, data=params,
        headers={
            'Content-type': 'application/x-www-form-urlencoded',
            'User-agent': 'noReCAPTCHA Python'
        }
    )

    httpresp = urlopen(req)

    try:
        res = force_text(httpresp.read())
        return_values = json.loads(res)
    except (ValueError, TypeError):
        return RecaptchaResponse(
            is_valid=False,
            error_codes=['json-read-issue']
        )
    except:
        return RecaptchaResponse(
            is_valid=False,
            error_codes=['unknown-network-issue']
        )
    finally:
        httpresp.close()

    return_code = return_values.get("success", False)
    error_codes = return_values.get('error-codes', [])
    logger.debug("%s - %s" % (return_code, error_codes))

    if return_code is True:
        return RecaptchaResponse(is_valid=True)
    else:
        return RecaptchaResponse(is_valid=False, error_codes=error_codes)
