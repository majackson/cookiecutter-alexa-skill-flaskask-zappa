from {{cookiecutter.project_slug}} import app

from flask_ask import Ask, statement

ask = Ask(app, '/')


@ask.launch
def launch():
    return hello_world_statement()


@ask.intent("HelloWorldIntent")
def hello_world_statement():
    return statement(_hello_world())


@app.route('/hello')
def hello_world_web():
    return _hello_world()


def _hello_world():
    return "Hello, world!"

