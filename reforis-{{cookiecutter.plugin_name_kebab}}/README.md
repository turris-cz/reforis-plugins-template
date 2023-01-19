# reForis {{cookiecutter.name}} Plugin

{{cookiecutter.description}}

To learn more about the plugin system see documentation of [reForis](https://gitlab.nic.cz/turris/reforis).

## Installing reForis Python package

By default, the latest version of the reForis package is automatically installed
when executing the `make prepare-dev` command. If you wish to use the
development (editable) version from a local directory, run `make
install-local-reforis`. It assumes that reForis is in the `reforis` directory
alongside the plugin directory.

Please note that you still need to upload the reForis code to the router to
consider changes.
