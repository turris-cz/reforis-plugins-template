{{ cookiecutter.license_js }}

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
