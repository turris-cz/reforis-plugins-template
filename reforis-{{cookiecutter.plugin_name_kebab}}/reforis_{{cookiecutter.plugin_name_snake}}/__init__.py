#  Copyright (C) 2020-2023 CZ.NIC z.s.p.o. (https://www.nic.cz/)
#
#  This is free software, licensed under the GNU General Public License v3.
#  See /LICENSE for more information.

from pathlib import Path
from http import HTTPStatus

from flask import Blueprint, current_app, jsonify, request
from flask_babel import gettext as _

from reforis.foris_controller_api.utils import validate_json, APIError

# pylint: disable=invalid-name
blueprint = Blueprint(
    '{{cookiecutter.plugin_name_camel}}',
    __name__,
    url_prefix='/{{cookiecutter.plugin_url_prefix}}/api',
)

BASE_DIR = Path(__file__).parent

# pylint: disable=invalid-name
{{cookiecutter.plugin_name_snake}} = {
    'blueprint': blueprint,
    # Define {python_module_name}/js/app.min.js
    # See https://gitlab.labs.nic.cz/turris/reforis/reforis-distutils/blob/master/reforis_distutils/__init__.py#L11
    'js_app_path': 'reforis_{{cookiecutter.plugin_name_snake}}/js/app.min.js',
    'translations_path': BASE_DIR / 'translations',
}


@blueprint.route('/example', methods=['GET'])
def get_example():
    return jsonify(current_app.backend.perform('example_module', 'example_action'))


@blueprint.route('/example', methods=['POST'])
def post_example():
    validate_json(request.json, {'modules': list})

    response = current_app.backend.perform('example_module', 'example_action', request.json)
    if response.get('result') is not True:
        raise APIError(_('Cannot create entity'), HTTPStatus.INTERNAL_SERVER_ERROR)

    return jsonify(response), HTTPStatus.CREATED
