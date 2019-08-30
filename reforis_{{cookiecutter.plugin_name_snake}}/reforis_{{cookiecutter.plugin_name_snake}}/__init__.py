#  Copyright (C) 2019 CZ.NIC z.s.p.o. (http://www.nic.cz/)
#
#  This is free software, licensed under the GNU General Public License v3.
#  See /LICENSE for more information.

from flask import Blueprint, current_app, jsonify

blueprint = Blueprint('{{cookiecutter.plugin_name_camel}}', __name__, url_prefix='{{cookiecutter.plugin_url}}/api')

{{cookiecutter.plugin_name_snake}} = {
    'blueprint': blueprint,
    'js_app_path': '{{cookiecutter.plugin_name_snake}}/app.min.js'
}


@blueprint.route('/example', methods=['GET'])
def list_modules():
    return jsonify(current_app.backend.perform('example_module', 'example_action'))
