import os

from setuptools import setup, find_packages

SETUP_DIR = os.path.dirname(os.path.abspath(__file__))
EXCLUDE_FROM_PACKAGES = ['vtmarketplace.conf.project_settings',
                         'vtmarketplace.bin']


# Dynamically calculate the version based on django.VERSION.
version = __import__('vtmarketplace').get_version()


# Setup should be run from any extracted folder
os.chdir(SETUP_DIR)


# Getting setup's long descripton from README.md
with open(os.path.join(SETUP_DIR, 'README.md')) as readme:
    README = readme.read()


setup(name='VTMarketPlace',
      version=version,
      url='https://github.com/mysteryjeans/vtmarketplace',
      author='VTMarketPlace',
      author_email='xyz@vt.edu',
      description='One stop destination for VT Student Marketplace',
      long_description=README,
      license='GPLv2',
      packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
      include_package_data=True,
      scripts=['vtmarketplace/bin/vtmarketplace-admin.py'],
      install_requires=['Django>=1.8.13,<1.10',
                        'django-pipeline>=1.6',
                        'Pillow>=2.7.0',
                        'paypalrestsdk>=1.8',
                        'stripe>=1.21.0',
                        'pytz>=2014.10',
                        'sorl-thumbnail>=12.3'])
