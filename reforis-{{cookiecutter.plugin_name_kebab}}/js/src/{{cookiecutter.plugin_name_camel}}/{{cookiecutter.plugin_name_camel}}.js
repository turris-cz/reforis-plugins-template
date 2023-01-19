/*
 * Copyright (C) 2020-2023 CZ.NIC z.s.p.o. (https://www.nic.cz/)
 *
 * This is free software, licensed under the GNU General Public License v3.
 * See /LICENSE for more information.
 */

import React, { useEffect } from "react";

import { useAPIGet } from "foris";

import API_URLs from "API";

export default function {{cookiecutter.plugin_name_camel}}() {
    const [, getExample] = useAPIGet(API_URLs.example);
    useEffect(() => {
        getExample();
    }, [getExample]);

    return (
        <>
            <h1>{{cookiecutter.name|title}}</h1>
            <p>{_("Add your components here")}</p>
        </>
    );
}
