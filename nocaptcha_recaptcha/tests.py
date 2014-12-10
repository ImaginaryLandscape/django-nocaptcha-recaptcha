import os
from django.forms import Form
from django.test import TestCase
from . import fields


class TestForm(Form):
    captcha = fields.NoReCaptchaField(gtag_attrs={'data-theme': 'dark'})


class TestCase(TestCase):
    def setUp(self):
        os.environ['NORECAPTCHA_TESTING'] = 'True'

    def test_envvar_enabled(self):
        form_params = {'g-recaptcha-response': 'PASSED'}
        form = TestForm(form_params)
        self.assertTrue(form.is_valid())

    def test_envvar_disabled(self):
        os.environ['NORECAPTCHA_TESTING'] = 'False'
        form_params = {'g-recaptcha-response': 'PASSED'}
        form = TestForm(form_params)
        self.assertFalse(form.is_valid())

    def tearDown(self):
        del os.environ['NORECAPTCHA_TESTING']
