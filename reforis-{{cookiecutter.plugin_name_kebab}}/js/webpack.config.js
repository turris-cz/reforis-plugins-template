/*
 * Copyright (C) 2019 CZ.NIC z.s.p.o. (http://www.nic.cz/)
 *
 * This is free software, licensed under the GNU General Public License v3.
 * See /LICENSE for more information.
 */

const path = require("path");

module.exports = () => ({
    mode: "development",
    entry: "./src/app.js",
    output: {
        // Build js app to ../reforis_static{python_module_name}/js/app.min.js
        // See https://gitlab.labs.nic.cz/turris/reforis/reforis-distutils/blob/master/reforis_distutils/__init__.py#L11
        filename: "app.min.js",
        path: path.join(__dirname, "../reforis_static/reforis_{{cookiecutter.plugin_name_snake}}/"),
    },
    resolve: {
        modules: [
            path.resolve(__dirname, "./src"),
            path.resolve(__dirname, "./node_modules")
        ]
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: "babel-loader",
            },
            {
                test: /\.css$/,
                use: ["style-loader", "css-loader"],
            },
        ],
    },
    externals: {
        react: "React",
        "react-dom": "ReactDOM",
    },
});