import os
import json

from django.forms import Form
from django.test import TestCase

import mock

from nocaptcha_recaptcha import fields, client


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

    @mock.patch('nocaptcha_recaptcha.client.urlopen')
    def test_client_submit_empty_input(self, mock_urlopen):
        """
        Should return False if input is empty string
        """
        result = client.submit('', '', '')
        self.assertFalse(result.is_valid)
        self.assertEqual(['incorrect-captcha-sol'], result.error_codes)

    @mock.patch('nocaptcha_recaptcha.client.urlopen')
    def test_client_submit_correct(self, mock_urlopen):
        """
        Should return True if response is correct
        """
        mock_resp = mock.Mock()
        mock_resp.read.return_value = json.dumps(
            {'success': True, 'error-codes': []})
        mock_urlopen.return_value = mock_resp
        result = client.submit('a', 'a', 'a')
        self.assertTrue(result.is_valid)
        self.assertEqual(result.error_codes, None)

    @mock.patch('nocaptcha_recaptcha.client.urlopen')
    def test_client_submit_response_not_json(self, mock_urlopen):
        """
        Should return json read error if response is not json
        """
        mock_resp = mock.Mock()
        mock_resp.read.return_value = "{'success': True, 'error-codes': []}"
        mock_urlopen.return_value = mock_resp
        result = client.submit('a', 'a', 'a')
        self.assertFalse(result.is_valid)
        self.assertEqual(result.error_codes, ['json-read-issue'])

    @mock.patch('nocaptcha_recaptcha.client.urlopen')
    def test_client_submit_response_incorrect(self, mock_urlopen):
        """
        Should return false if response is incorrect
        """
        mock_resp = mock.Mock()
        mock_resp.read.return_value = json.dumps(
            {'success': False, 'error-codes': ['ERROR']})
        mock_urlopen.return_value = mock_resp
        result = client.submit('a', 'a', 'a')
        self.assertFalse(result.is_valid)
        self.assertEqual(result.error_codes, ['ERROR'])

    def tearDown(self):
        del os.environ['NORECAPTCHA_TESTING']
