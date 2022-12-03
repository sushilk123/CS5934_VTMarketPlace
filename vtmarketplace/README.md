VTMarketplace
========

Virginia Tech MarketPlace is a one stop shop for all VT students to buy and sell used items. It is designed specifically for the VT students to limit the user base and reinforce trust in transactions.
It is a platform where sellers can come together to sell their products or services to a curated customer base. Sellers have a place to gain visibility and sell their products, and the marketplace buyers can get the items at a cheaper and better price

## Features

- Responsive design
- Multiple payment methods
- Paypal & Strip payment gateways integration
- Multiple currency support & rate conversion
- Tax calculation & shipping cost on checkout
- Pages & footer links
- Categories, breadcrumbs and search as unified field
- Built on [Django](https://www.djangoproject.com/), [Bootstrap](https://getbootstrap.com/) & [LESS](http://lesscss.org/)
- Built as Django apps in the first place
- Compression & minification of static content CSS & JS
- Cache refresh/invalidation for static contents CSS & JS


## Setting up VTMarketplace e-commerce as Django project


When you have enough testing on prepopulated data in demo projects, starting your own site from scratch with basic data prepopulated.

Create a new virtualenv for your own e-commerce project

```
$ virtualenv vtmarketplace_env && source vtmarketplace_env/bin/activate
```

Get copy of latest version of VTMarketplace from Github.

```
$ git clone https://github.com/sushilk123/CS5934_VTMarketPlace.git && cd vtmarketplace
```

Install Django and other packages dependencies using requirements.txt in your virtualenv. VTMarketplace also requires Node.js packages, see details below.

```
$ pip install -r requirements.txt
```

Create database schema by running migrate command, by default Django project use SQLite, if you are new to databases this is good choice to start with. Migrate command will also load initial data in database as well.

```
$ python manage.py migrate
```

If you have exported repository clone path then install Django & other packages dependencies using requirements.txt in your virtualenv first and then create new project site. vtmarketplace also requires Node.js packages, see details below.

## Node.js packages dependency and installation

Django-Pipeline settings is configured to use [LESS](http://lesscss.org/#using-less-installation) & [Yuglify](https://github.com/yui/yuglify) node.js packages for static files preprocessing & compression. When you deploy your site with collectstatic command these packages will be called. You can install both packages with [npm](https://www.npmjs.org/) (node.js package manager).

```
$ npm install -g less yuglify
```

## Running development server for your e-commerce project

Assuming you have installed [node.js](http://nodejs.org/) & packages, let's verify that your site works, run development server and visit [http://127.0.0.1:8000](http://127.0.0.1:8000), you will see products catalog index pages with no products and categories

```
$ python manage.py runserver
```


## Development

VTMarketplace is yet to develop some core features:

- Dashboard
- Unit tests

## Built With

- [Django](https://github.com/django/django) &mdash; Web development framework for python, we utilizes full stack.
- [LESS](https://github.com/less/less.js) &mdash; Our styling totally done in LESS, a preprocessor for CSS.
- [Django-Pipeline](https://github.com/cyberdelia/django-pipeline) &mdash; We use django-pipeline to compile & compress LESS and also Javascript before deployment.
- [PostgreSQL](http://www.postgresql.org/) &mdash; Our primary database is PostgreSQL, although project intended to support all databases that Django supports.


