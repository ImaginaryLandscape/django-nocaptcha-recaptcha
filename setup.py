import os
import sys
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


if sys.version_info > (3, 3):
    django_setuptest = 'python3-django-setuptest'
else:
    django_setuptest = 'django-setuptest>=0.1'


setup(
    name='django-nocaptcha-recaptcha',
    version='0.0.20',
    description='Django nocaptcha recaptcha form field/widget app.',
    long_description=read('README.md'),
    author='Imaginary Landscape',
    author_email='jjasinski@imgescape.com',
    keywords=['django', 'recaptcha', 'field', 'nocaptcha'],
    license='BSD',
    url='https://github.com/ImaginaryLandscape/django-nocaptcha-recaptcha',
    packages=find_packages(),
    tests_require=[
        django_setuptest,
        'mock',
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
