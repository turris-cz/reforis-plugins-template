/*
 * Copyright (C) 2019 CZ.NIC z.s.p.o. (http://www.nic.cz/)
 *
 * This is free software, licensed under the GNU General Public License v3.
 * See /LICENSE for more information.
 */

import React from "react";

export default function {{cookiecutter.plugin_name_camel}}() {
    return (
        <>
            <h1>{{cookiecutter.name|title}}</h1>
            <p>{_("Add your components here")}</p>
        </>
    );
}