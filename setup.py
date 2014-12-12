import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-nocaptcha-recaptcha',
    version='0.0.17',
    description='Django nocaptcha recaptcha form field/widget app.',
    long_description=read('README.md'),
    author='Imaginary Landscape',
    author_email='jjasinski@imgescape.com',
    keywords = ['django', 'recaptcha', 'field', 'nocaptcha'],
    license='BSD',
    url='https://github.com/ImaginaryLandscape/django-nocaptcha-recaptcha',
    packages=find_packages(),
    tests_require=[
        'django-setuptest>=0.1',
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
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
