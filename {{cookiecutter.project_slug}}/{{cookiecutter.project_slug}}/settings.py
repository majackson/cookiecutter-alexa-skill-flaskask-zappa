"Place flask settings in this file."

import os

from distutils.util import strtobool

from {{cookiecutter.project_slug}} import app

PRODUCTION = bool(strtobool(os.environ.get('PRODUCTION', 'False')))

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



