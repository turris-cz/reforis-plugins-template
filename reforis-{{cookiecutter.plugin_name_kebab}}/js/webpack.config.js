{{ cookiecutter.license_js }}

const path = require("path");

module.exports = () => ({
    mode: "development",
    entry: "./src/app.js",
    output: {
        // Build js app to ../reforis_static{python_module_name}/app.min.js
        // See https://gitlab.labs.nic.cz/turris/reforis/reforis-distutils/blob/master/reforis_distutils/__init__.py#L11
        filename: "app.min.js",
        path: path.join(
            __dirname,
            "../reforis_static/reforis_{{cookiecutter.plugin_name_snake}}/js/"
        ),
    },
    resolve: {
        modules: [
            path.resolve(__dirname, "./src"),
            path.resolve(__dirname, "./node_modules"),
        ],
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules\/(?!foris)/,
                loader: "babel-loader",
            },
            {
                test: /\.css$/,
                use: ["style-loader", "css-loader"],
            },
        ],
    },
    // Equal to peerDependencies in package.json
    externals: {
        "prop-types": "PropTypes",
        react: "React",
        "react-dom": "ReactDOM",
        "react-router-dom": "ReactRouterDOM",
    },
});
