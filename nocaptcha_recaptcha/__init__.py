import pkg_resources

__version__ = pkg_resources.require("django-nocaptcha-recaptcha")[0].version

from .fields import NoReCaptchaField
from .widgets import NoReCaptchaWidget
