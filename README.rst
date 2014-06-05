|logo| |travis| |pypi| |coverage|

Create your landing page with all the common features: A release date counter,
email subscribers, social integration, segmentation, etc.

Features
========

* Based on bootstrap3.
* Integrate it easily with your existing project.
* Customize your landing page using your own templates.
* Email newsletters, collect subscriber and send them newsletter from the django administration interface.
* Not online yet? Easy render a countdown.
* Integrate with as a `Django-CMS`_ plugins.
* Easy to use templates to enable Social Integration.
* Segmentate your landing page by using tags.
* Easy to extend form from settings.
* Not enough for you? All views are Class Based Views and can be used in your project with out registering the default urls.

How to Install
==============

Get the code
------------

Getting the code for the latest stable release use `pip`. ::

   $ pip install django-rocket

Install in your project
-----------------------

Then register `django_rocket`, in the `INSTALLED_APPS` section of
your project's settings. ::

  INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.contenttypes',

    'django_rocket',
  )

Add at these following lines to your project's urlpatterns in the last position
to enable the landing page. ::

  url(r'^', include('django_rocket.urls')),

Remember to enable the `django.contrib.admin` site in the urls.py of
your project if you haven't done it yet for having the edition capabilities.

Syncing the database
--------------------

Now that you have everything set up, simply run the following in your
project directory to sync the models with the database. ::

  $ python manage.py syncdb

If you are using South to manage your database, you will have to do the
following. ::

  $ python manage.py syncdb --migrate

For more detailed documentation go to http://django-rocket.readthedocs.org/

|bitdeli|


.. |logo| image:: https://raw.github.com/mariocesar/django-rocket/master/logo.png

.. |travis| image:: https://travis-ci.org/mariocesar/django-rocket.png?branch=master
    :target: https://travis-ci.org/mariocesar/django-rocket

.. |pypi| image:: https://badge.fury.io/py/django-rocket.png
    :target: http://badge.fury.io/py/django-rocket

.. |coverage| image:: https://coveralls.io/repos/mariocesar/django-rocket/badge.png
    :target: https://coveralls.io/r/mariocesar/django-rocket

.. |bitdeli| image:: https://d2weczhvl823v0.cloudfront.net/mariocesar/django-rocket/trend.png
    :target: https://bitdeli.com/free
    :alt: Bitdeli Badge

.. _`Django-CMS`: http://django-rocket.readthedocs.org/en/latest/getting-started/configuration.html#django-cms
