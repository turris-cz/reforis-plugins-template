/*
 * Copyright (C) 2019 CZ.NIC z.s.p.o. (http://www.nic.cz/)
 *
 * This is free software, licensed under the GNU General Public License v3.
 * See /LICENSE for more information.
 */

import {{cookiecutter.plugin_name_camel}} from "./{{cookiecutter.plugin_name_snake}}/{{cookiecutter.plugin_name_camel}}";

const {{cookiecutter.plugin_name_camel}}Plugin = {
    name: _("{{cookiecutter.name|title}}"),
    submenuId: "administration",
    weight: 100,
    path: "{{cookiecutter.plugin_url}}",
    component: {{cookiecutter.plugin_name_camel}},
};

ForisPlugins.push({{cookiecutter.plugin_name_camel}}Plugin);