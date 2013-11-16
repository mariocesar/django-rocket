from django_buzz import __version__, __author__, __email__, __license__

from setuptools import setup, find_packages

README = open('README.rst').read()
# Second paragraph has the short description
description = README.split('\n')[1]

setup(
    name='django-buzz',
    version=__version__,
    description=description,
    long_description=README,
    author=__author__,
    author_email=__email__,
    license=__license__,
    url='https://github.com/mariocesar/django-buzz',
    download_url='https://pypi.python.org/pypi/django-buzz',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'django>=1.5.5,<1.7',
    ],
    zip_safe=False,
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django'
    ],
)