# reForis plugins template

## Naming convetion
When creating new repository please use `reforis_{{plugin_name}}` format for the path. It should be the same name as for Python module that would be a part of the plugin.

## Development installation

1. Install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
    ```bash
    $ pip3 install cookiecutter
    ```

2. Install template and fill template variables
    ```bash
    $ cookiecutter https://gitlab.labs.nic.cz/turris/reforis/plugins-template
    ```
    If you want to use template from specific branch e.g. `dev`
    ```bash
    $ cookiecutter https://gitlab.labs.nic.cz/turris/reforis/plugins-template --checkout dev
    ```
    If `cookiecutter` command is not available try `python3 -m cookiecutter`.

3. Install npm dependencies
    ```bash
    $ cd reforis_{{plugin_name}}
    $ make preapare-dev
    ```

4. Build JS
    ```bash
    $ make build-js
    ```

5. Sync plugin directory with router - copy repository to `/tmp/reforis_{{plugin_name}}/`

6. Install plugin **on the router**
    ```bash
    $ cd /tmp/reforis_{{plugin_name}}/
    $ make install
    ```

## Version control
Please note that the git repository is not automatically created. If you wish to use one it's advised to add `repository` section to `package.json`.
