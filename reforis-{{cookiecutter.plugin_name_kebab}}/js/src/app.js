/*
 * Copyright (C) 2020 CZ.NIC z.s.p.o. (http://www.nic.cz/)
 *
 * This is free software, licensed under the GNU General Public License v3.
 * See /LICENSE for more information.
 */

import {{cookiecutter.plugin_name_camel}} from "./{{cookiecutter.plugin_name_camel}}/{{cookiecutter.plugin_name_camel}}";

const {{cookiecutter.plugin_name_camel}}Plugin = {
    name: _("{{cookiecutter.name|title}}"),
    weight: 100,
    submenuId: "{{cookiecutter.plugin_url_prefix}}",
    path: "/{{cookiecutter.plugin_url_prefix}}",
    component: {{cookiecutter.plugin_name_camel}},
    icon: "cube",
};

ForisPlugins.push({{cookiecutter.plugin_name_camel}}Plugin);
