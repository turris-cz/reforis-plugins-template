{{ cookiecutter.license_js }}

import { REFORIS_URL_PREFIX } from "foris";

const API_URL_PREFIX = `${REFORIS_URL_PREFIX}/{{cookiecutter.plugin_url_prefix}}/api`;

const API_URLs = new Proxy(
    {
        example: "/example",
    },
    {
        get: (target, name) => `${API_URL_PREFIX}${target[name]}`,
    }
);

export default API_URLs;
