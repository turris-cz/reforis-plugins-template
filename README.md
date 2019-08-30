# reForis plugins template

## Development installation

### Install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)

### Install template and fulfill template variables.
```bash
>>> cookiecutter https://gitlab.labs.nic.cz/turris/reforis/plugins-template
```

### Install npm dependencies
```bash
>>> cd reforis_{{plugin_name}}
>>> make preapare_dev
```

### Build JS 
```bash
>>> make build-js
```

### Sync plugin directory with a router

### Install plugin **on the router**
```bash
>>> make install
```
