from reforis.test_utils import get_mocked_client

def get_mocked_{{cookiecutter.plugin_name_snake}}_client(*args, **kwargs):
    return get_mocked_client('reforis_{{cookiecutter.plugin_name_snake}}', *args, *kwargs)
