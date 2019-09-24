import pytest
from flask import Flask

from reforis_{{cookiecutter.plugin_name_snake}} import blueprint


@pytest.fixture(scope="module")
def app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    app.backend = None
    return app
