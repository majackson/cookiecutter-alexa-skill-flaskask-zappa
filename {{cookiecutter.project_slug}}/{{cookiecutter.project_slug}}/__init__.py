from flask import Flask

app = Flask(__name__)

from {{cookiecutter.project_slug}} import settings, models, views  # NOQA
