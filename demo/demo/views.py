from django.views.generic import FormView
from django import forms
from django.core.urlresolvers import reverse_lazy
from nocaptcha_recaptcha.fields import NoReCaptchaField

class DemoForm(forms.Form):
    username = forms.CharField(required=True)
    captcha = NoReCaptchaField(gtag_attrs={'data-theme':'dark'})


class DemoView(FormView):
    form_class = DemoForm
    success_url = reverse_lazy('success')
    
    def form_valid(self, form):
        return super(DemoView, self).form_valid(form)