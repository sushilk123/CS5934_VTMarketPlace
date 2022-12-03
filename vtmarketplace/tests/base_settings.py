"""
Base settings for all tests
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vtmarketplace_test_settings_key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'vtmarketplace.urls'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


################## vtmarketplace #########################
#####################################################

# vtmarketplace e-commerce settings for Django project
# Customize these settings only if you know

# Django authentication app extended by vtmarketplace in Django way
# To implement your own custom auth user model, extend
# vtmarketplace.accounts.AbstractUser instead and change AUTH_USER_MODEL
# similarly. vtmarketplace will adopt new AUTH_USER_MODEL seemlessly
AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

# vtmarketplace apps configuration required for Django
INSTALLED_APPS += (
    'vtmarketplace',
    'vtmarketplace.geo',
    'vtmarketplace.pages',
    'vtmarketplace.accounts',
    'vtmarketplace.catalog',
    'vtmarketplace.sales',
    'vtmarketplace.financial',
    'vtmarketplace.payments',
)

# DOMAIN will be used in link generation specially in emails
DOMAIN = '127.0.0.1:8000'

# SITE_NAME it will be used in all pages, this is the name of your website
SITE_NAME = 'VTMarketPlace'

# SITE_TITLE for index pages of your website
SITE_TITLE = 'VTMarketPlace'

# Meta description for SEO
SITE_DESCRIPTION = 'The e-commerce solution for VT Students'

# COPYRIGHT statement for all pages
COPYRIGHT = 'Copyright &copy; 2022 VTMarketPlace. All rights reserved.'

# SUPPORT_EMAIL address for bugs and error reporting
SUPPORT_EMAIL = 'vtmarketplace@vt.edu'


# Email Server settings for sending notifications & confirmations emails
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = r''


################ Django-Pipeline #####################
######################################################

# vtmarketplace uses django-pipeline for LESS & Javascript
# preprocessing, compression and versioning.

# When collectstatic called during deployment LESS & Javascript will be
# compiled, compressed and versioned before copying to static folder

# Django-Pipeline app required by vtmarketplace
INSTALLED_APPS += ('pipeline',)

# LESS compiler configuration for django-pipeline
PIPELINE_COMPILERS = ('pipeline.compilers.less.LessCompiler',)

# LESS & Javascript static files serving in development
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Custom Javascript needs to be in global scope
# in order for vtmarketplace to work properly
PIPELINE_DISABLE_WRAPPER = True


# CSS configurations for django-pipeline
# All LESS styles configured for vtmarketplace defined
# You can append your LESS configurations here.
PIPELINE_CSS = {
    # vtmarketplace app LESS styles
    'base': {
        'source_filenames': (
            'vtmarketplace/css/base.less',
        ),
        'output_filename': 'vtmarketplace/css/base.css'
    },
    # vtmarketplace.catalog LESS styles for products catalog
    'catalog': {
        'source_filenames': (
            'catalog/css/catalog.less',
        ),
        'output_filename': 'catalog/css/catalog.css'
    },
    # Font-Awesome icons serve mostly
    'font-awesome': {
        'source_filenames': (
            'catalog/css/font-awesome/css/font-awesome.min.css',
        ),
        'output_filename': 'catalog/css/font-awesome/css/font-awesome.min.css'
    },
    # vtmarketplace.sales LESS styles for checkout pages
    'sales': {
        'source_filenames': (
            'sales/css/sales.less',
        ),
        'output_filename': 'sales/css/sales.css'
    },
    # vtmarketplace.pages LESS styles for flat pages
    'pages': {
        'source_filenames': (
            'pages/css/pages.less',
        ),
        'output_filename': 'pages/css/pages.css'
    }
}


# Javascript configuration for django-pipeline
# vtmarketplace app's Javascript compressed & versioned before deployment
# Simply add your project or apps Javascript here
PIPELINE_JS = {
    # vtmarketplace: Base javascript include in every page
    'base': {
        'source_filenames': (
            'vtmarketplace/scripts/jquery-ajax.js',
            'vtmarketplace/scripts/jquery-utils.js',
        ),
        'output_filename': 'vtmarketplace/scripts/base.js',
    },
    # vtmarketplace.catalog: Javascript for product catalog pages
    'catalog_base': {
        'source_filenames': (
            'catalog/scripts/jquery.catalog_base.js',
        ),
        'output_filename': 'catalog/scripts/catalog_base.js',
    },
    'search_products': {
        'source_filenames': (
            'catalog/scripts/jquery.search_products.js',
        ),
        'output_filename': 'catalog/scripts/search_products.js',
    },
    'product_detail': {
        'source_filenames': (
            'catalog/scripts/jquery.scrollTo.js',
            'catalog/scripts/jquery.serialScroll.js',
            'catalog/scripts/jquery.elevatezoom.js',
            'catalog/scripts/jquery.product_detail.js',
        ),
        'output_filename': 'catalog/scripts/product_detail.js',
    },
    'sales_checkout_order': {
        'source_filenames': (
            'sales/scripts/jquery.creditCardValidator.js',
            'sales/scripts/jquery.maskedinput.js',
            'sales/scripts/jquery.checkout_order.js',
        ),
        'output_filename': 'sales/scripts/sales_checkout_order.js',
    }
}