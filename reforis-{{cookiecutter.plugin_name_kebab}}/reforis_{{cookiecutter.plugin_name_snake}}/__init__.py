#  Copyright (C) 2019 CZ.NIC z.s.p.o. (http://www.nic.cz/)
#
#  This is free software, licensed under the GNU General Public License v3.
#  See /LICENSE for more information.

from flask import Blueprint, current_app, jsonify

# pylint: disable=invalid-name
blueprint = Blueprint(
    '{{cookiecutter.plugin_name_camel}}',
    __name__,
    url_prefix='{{cookiecutter.plugin_url}}/api',
)

# pylint: disable=invalid-name
{{cookiecutter.plugin_name_snake}} = {
    'blueprint': blueprint,
    # Define {python_module_name}/js/app.min.js
    # See https://gitlab.labs.nic.cz/turris/reforis/reforis-distutils/blob/master/reforis_distutils/__init__.py#L11
    'js_app_path': 'reforis_{{cookiecutter.plugin_name_snake}}/js/app.min.js'
}


@blueprint.route("/example", methods=["GET"])
def get_example():
    return jsonify(current_app.backend.perform("example_module", "example_action"))
