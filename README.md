[![Build Status](https://travis-ci.org/ImaginaryLandscape/django-nocaptcha-recaptcha.svg?branch=master)](https://travis-ci.org/ImaginaryLandscape/django-nocaptcha-recaptcha)

# SUMMARY

Add new-style Google ReCaptcha widgets to your Django forms simply by adding a 
NoReCaptchaField field to said forms. 

# ABOUT 

In late 2014, Google updated their ReCaptcha service, changing its API.  The update significantly
changes the appearance and function of ReCaptcha.  This has been referred to as
ReCaptcha 2 or "nocaptcha recaptcha". 

This module is intended to be a successor to django-recaptcha to support the new style 
Google Recaptcha.  It borrows a lot of the logic from the django-recaptcha, but has been
updated to support the Google change. 

For the Google documentation for this service, visit the following: 

    https://developers.google.com/recaptcha/intro
   
The original django-recaptcha project is located at the following location:

    https://github.com/praekelt/django-recaptcha

# FEATURES

 - Implements Google's New "NoCaptcha ReCaptcha Field"
 - Uses the fallback option for browsers without JavaScript
 - Easy to add to a Form via a FormField
 - Works similar to django-recaptcha 
 - Working demo projects
 - Works with Python 2.7 and 3.4

# INSTALL

    pip install django-nocaptcha-recaptcha

# CONFIGURE 

Add nocaptcha_recaptcha to your INSTALLED_APPS setting
    
Add the following to settings.py
    
    Required settings: 
    NORECAPTCHA_SITE_KEY  (string) = the Google provided site_key
    NORECAPTCHA_SECRET_KEY (string) = the Google provided secret_key 
    
    Optional Settings:
    NORECAPTCHA_VERIFY_URL (string) = reCaptcha api endpoint for verification.
        Best to leave this as the default setting.
        Default is https://www.google.com/recaptcha/api/siteverify
    NORECAPTCHA_WIDGET_TEMPLATE (string) = location for the widget template.  
        Default is nocaptcha_recaptcha/widget.html


Add the field to a form that you want to protect.

	from nocaptcha_recaptcha.fields import NoReCaptchaField
	
	class DemoForm(forms.Form):
	    .....
	    captcha = NoReCaptchaField()
	    

Add Google's JavaScript library to your base template or elsewhere, so it is
available on the page containing the django form.

    <script src="https://www.google.com/recaptcha/api.js" async defer></script>	    


(optional)
You can customize the field.  
	
- You can add attributes to the g-recaptcha div tag through the following
     
     captcha = NoReCaptchaField(gtag_attrs={'data-theme':'dark'}))
     
- You can override the template for the widget like you would any
  other django template. 


# DEMO PROJECT 

The demo project includes a fully working example of this module. 
To use it, run the following:
 
    cd demo
    export NORECAPTCHA_SITE_KEY="<your site key>"
    export NORECAPTCHA_SECRET_KEY="<your secret key>"
    ./manage.py runserver 
   
    # in a browser, visit http://localhost:8000
     
# TESTING

    python setup.py test
