from {{cookiecutter.project_slug}} import views


def test_hello_world():
    resp = views._hello_world()
    assert "Hello, world!" in resp

