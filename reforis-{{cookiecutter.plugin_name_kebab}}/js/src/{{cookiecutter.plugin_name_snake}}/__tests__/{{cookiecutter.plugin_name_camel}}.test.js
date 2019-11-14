/*
 * Copyright (C) 2019 CZ.NIC z.s.p.o. (http://www.nic.cz/)
 *
 * This is free software, licensed under the GNU General Public License v3.
 * See /LICENSE for more information.
 */

import React from "react";
import mockAxios from "jest-mock-axios";
import { render } from "foris/testUtils/customTestRender";

import {{cookiecutter.plugin_name_camel}} from "../{{cookiecutter.plugin_name_camel}}";

describe("<{{cookiecutter.plugin_name_camel}} />", () => {
    it("should render component", () => {
        const { getByText } = render(<{{cookiecutter.plugin_name_camel}} />);
        expect(getByText("{{cookiecutter.name|title}}")).toBeDefined();
        expect(mockAxios.get).toBeCalledWith("reforis/{{cookiecutter.plugin_url_prefix}}/api/example", expect.anything());
    });
});
