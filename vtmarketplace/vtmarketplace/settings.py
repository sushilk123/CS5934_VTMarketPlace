
import os

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
# DOORSALE_APPS = (
#     'vtmarketplace',
#     'vtmarketplace.geo',
#     'vtmarketplace.pages',
#     'vtmarketplace.accounts',
#     'vtmarketplace.catalog',
#     'vtmarketplace.sales',
#     'vtmarketplace.financial',
#     'vtmarketplace.payments',
# )
DOORSALE_APPS = (
    'vtmarketplace',
    'vtmarketplace.geo',
    'vtmarketplace.pages',
    'vtmarketplace.accounts',
    'vtmarketplace.catalog',
    'vtmarketplace.sales',
    'vtmarketplace.financial',
    'vtmarketplace.payments',
)

# Thumbnail generator app for vtmarketplace
DOORSALE_APPS += (
    'sorl.thumbnail',
)
# Raise thumbnail errors and send it via emails
THUMBNAIL_DEBUG = True

# vtmarketplace uses django-pipeline for LESS & Javascript
# preprocessing, compression and versioning.
# When collectstatic called during deployment LESS & Javascript will be
# compiled, compressed and versioned before copying to static folder
DOORSALE_APPS += ('pipeline',)

# LESS & Javascript static files serving in development
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

# Pipeline finders for serving pipeline static files
from django.conf.global_settings import STATICFILES_FINDERS
STATICFILES_FINDERS += (
    'pipeline.finders.PipelineFinder',
)

# LESS compiler search paths for resources
# Always use relative paths in @import statements in LESS
# All resources in app's static directory will be available
# for LESS compiler
from vtmarketplace.utils.finders import get_static_paths
STATIC_PATHS = os.pathsep.join(get_static_paths(DOORSALE_APPS))
PIPELINE_LESS_ARGUMENTS = '--include-path="%s"' % STATIC_PATHS

PIPELINE = {
    'COMPILERS': (
        'pipeline.compilers.less.LessCompiler',
        ),
    'LESS_ARGUMENTS': '--include-path="%s"' % STATIC_PATHS,

    # CSS configurations for django-pipeline
    # All LESS styles configured for vtmarketplace defined
    # You can append your LESS configurations here.
    'STYLESHEETS': {
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
    },

    'DISABLE_WRAPPER': True,
    # Javascript configuration for django-pipeline
    # vtmarketplace app's Javascript compressed & versioned before deployment
    # Simply add your project or apps Javascript here
    'JAVASCRIPT': {
        # vtmarketplace: Base javascript include in every page
        'jquery_ajax': {
            'source_filenames': (
                'vtmarketplace/scripts/jquery-ajax.js',
            ),
            'output_filename': 'vtmarketplace/scripts/jquery-ajax.js',
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
}

# Views to render page from vtmarketplace.pages
PAGE_VIEWS = (('pages_base_page', 'Base View'),
              ('pages_catalog_page', 'Catalog View')
)
