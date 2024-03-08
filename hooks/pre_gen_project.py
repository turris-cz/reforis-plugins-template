import sys

plugin_name_camel = "{{ cookiecutter.plugin_name_camel }}"

if " " in plugin_name_camel:
    print(f"ERROR: {plugin_name_camel} cannot contain spaces!")
    sys.exit(1)
