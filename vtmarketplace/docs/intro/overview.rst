.. _ref-overview:

========
Overview
========

vtmarketplace is open source e-commerce solution, simplicity in designed is to thrive
sales, which are reaching to be production ready. It is built on top of Django_
Web-development framework for Python.

.. _Django: https://djangoproject.com/

vtmarketplace Apps
=============

vtmarketplace is set of Django `apps`_ similar to builtin apps like session, auth,
admin and etc, each app is design to serve specific purpose.

* ``vtmarketplace``: core app for base classes of views and templates and hold all urls

* ``vtmarketplace.geo``: contains models for country, state & addresses

* ``vtmarketplace.pages``: to serve static pages for about, contact and policy

* ``vtmarketplace.accounts``: extends Django auth model and also provide abstract classes

* ``vtmarketplace.catalog``: products catalog and listings

* ``vtmarketplace.sales``: order processing

* ``vtmarketplace.financial``: currency rate and conversion

* ``vtmarketplace.payments``: payment gateways like PayPal & Stripe

.. _apps: https://docs.djangoproject.com/en/stable/intro/reusable-apps/

Built With
==========

* Django_: web development framework for python, we utilizes full stack.

* LESS_: styling totally done in LESS, a preprocessor for CSS.

* Django-Pipeline_: we use django-pipeline to compile & compress LESS and also
  compress Javascript before deployment.

* PostgreSQL_: I would recommend to use PostgreSQL for production, but project
  intended to support all databases that Django supports. SQLite_ is good
  alternative for small sites, let say 1000 orders per week won't break a sweat,
  see limit_ for SQLite for more details, but it has lacks good tools for
  administration

.. _Django: https://www.djangoproject.com
.. _LESS: https://github.com/less/less.js
.. _Django-Pipeline: https://github.com/cyberdelia/django-pipeline
.. _PostgreSQL: http://www.postgresql.org
.. _SQLite: http://www.sqlite.org/
.. _limit: http://www.sqlite.org/limits.html
