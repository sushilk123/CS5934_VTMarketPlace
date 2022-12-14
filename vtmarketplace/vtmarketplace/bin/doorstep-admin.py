#!/usr/bin/env python
import os
import sys

from django.core import management


def configure_vtmarketplace(project_name):
    """
    Configures vtmarketplace settings in project
    """
    import vtmarketplace

    vtmarketplace_app_urls_path = os.path.join(
        os.path.dirname(vtmarketplace.__file__),
        'conf', 'project_settings', 'app_urls.py')

    project_urls_path = os.path.join(
        os.getcwd(),
        project_name,
        project_name,
        'urls.py'
    )

    vtmarketplace_app_settings_path = os.path.join(
        os.path.dirname(vtmarketplace.__file__),
        'conf', 'project_settings', 'app_settings.py')

    project_settings_path = os.path.join(
        os.getcwd(),
        project_name,
        project_name,
        'settings.py'
    )

    # Dumps all preconfigured settings of vtmarketplace apps
    # into projects settings file
    with open(vtmarketplace_app_settings_path, "r+") as f:
        app_settings = f.read()

    with open(project_settings_path, 'a+') as f:
        f.write(app_settings)

    # Replaceing project urls.py from vtmarketplace urls
    with open(vtmarketplace_app_urls_path, "r+") as f:
        app_urls = f.read()

    with open(project_urls_path, "a+") as f:
        f.write(app_urls)


if __name__ == "__main__":
    import vtmarketplace
    project_template = os.path.join(os.path.dirname(vtmarketplace.__file__),
        'conf', 'project_template',)

    has_template = False
    for arg in sys.argv:
        if '--template' == arg or arg.startswith('--template='):
            has_template = True

    if not has_template:
        sys.argv.append('--template=' + project_template)

    management.execute_from_command_line()
