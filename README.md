# reForis Plugins Template

## Naming convention

When creating a new repository, please use `reforis_{{plugin_name}}` format for
the path. It should be the same name as for Python module that would be a part
of the plugin.

## Development installation

1. Install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)

```bash
pip3 install cookiecutter
```

2. Install template and fill template variables

```bash
cookiecutter https://gitlab.nic.cz/turris/reforis/plugins-template
```

If you want to use the template from a specific branch, e.g., `dev`

```bash
cookiecutter https://gitlab.nic.cz/turris/reforis/plugins-template --checkout dev
```

If `cookiecutter` command is not available try `python3 -m cookiecutter`.

3. Install npm dependencies

```bash
cd reforis_{{plugin_name}}
make prepare-dev
```

4. Initialize translation languages. Check variable `LANGS` in Makefile for a
   list of languages before initiating translations.

```bash
make init-lang
```

5. Build JS

```bash
make build-js
```

6. Sync plugin directory with router - copy repository to
   `/tmp/reforis_{{plugin_name}}/`

7. Install the plugin **on the router**

```bash
cd /tmp/reforis_{{plugin_name}}/
make install
```

## Testing

To locally test the example plugin, you can use the `make` commands:

-   `test`
-   `lint`
-   `init-langs`

## Version control

Please note that the git repository is not automatically created. If you wish to
use one, it's advised to add a `repository` section to `package.json`.

## Dependencies

### Foris JS

[Foris JS](https://gitlab.nic.cz/turris/reforis/foris-js) is one of the
plugin's dependencies. For developers' convenience, its version is set to the
`latest` (in the `package.json` file). After creating a new plugin with the
template, it is recommended to fix the version, i.e., change the `latest` to the
actual version (e.g., `0.2.3`) so that breaking changes in the library won't
affect the new plugin in an undesired way.

### reForis

Most plugins would take advantage of reForis API utils, such as `APIError`
exception or `validate_json` function. As a consequence, `reForis` is installed
by `setup.py` (in Python's virtual environment) during development or testing
(CI). If you find yourself not using those utilities, feel free to remove that
dependency in your plugin.
