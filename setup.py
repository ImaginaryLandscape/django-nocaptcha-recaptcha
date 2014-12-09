
from setuptools import setup, find_packages
setup(
    name='django-nocaptcha-recaptcha',
    version='0.0.1',
    description='Django nocaptcha recaptcha form field/widget app.',
    long_description=open('README.md', 'r').read(),
    author='Imaginary Landscape',
    author_email='jjasinski@imgescape.com',
    license='BSD',
    url='http://github.com/ImaginaryLandscape/django-nocaptcha-recaptcha',
    packages=find_packages(),
    tests_require=[
        'django-setuptest>=0.1',
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
