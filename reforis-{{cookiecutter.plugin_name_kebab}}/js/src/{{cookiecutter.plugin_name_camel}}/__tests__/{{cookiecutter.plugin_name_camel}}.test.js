{{ cookiecutter.license_js }}

import React from "react";
import mockAxios from "jest-mock-axios";
import { render } from "foris/testUtils/customTestRender";

import {{cookiecutter.plugin_name_camel}} from "../{{cookiecutter.plugin_name_camel}}";

describe("<{{cookiecutter.plugin_name_camel}} />", () => {
    it("should render component", () => {
        const { getByText } = render(<{{cookiecutter.plugin_name_camel}} />);
        expect(getByText("{{cookiecutter.name|title}}")).toBeDefined();
        expect(mockAxios.get).toBeCalledWith("/reforis/{{cookiecutter.plugin_url_prefix}}/api/example", expect.anything());
    });
});
