from setuptools import find_packages, setup

from django_rocket import __author__, __email__, __license__, __version__

README = open("README.rst").read()

# Second paragraph has the short description
description = README.split("\n")[1]

setup(
    name="django-rocket",
    version=__version__,
    description=description,
    long_description=README,
    author=__author__,
    author_email=__email__,
    license=__license__,
    url="https://github.com/mariocesar/django-rocket",
    download_url="https://pypi.python.org/pypi/django-rocket",
    packages=find_packages(exclude=["tests", "example", "docs"]),
    include_package_data=True,
    install_requires=["django>=2.2"],
    zip_safe=False,
    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
