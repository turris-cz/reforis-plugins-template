from http import HTTPStatus

from utils import get_mocked_client


def test_get_example(app):
    backend_response = {"key": "value"}
    with get_mocked_client(app, backend_response) as client:
        response = client.get("{{cookiecutter.plugin_url}}/api/example")
    assert response.status_code == HTTPStatus.OK
    assert response.json == backend_response
