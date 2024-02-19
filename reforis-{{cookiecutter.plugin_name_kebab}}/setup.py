# !/usr/bin/env python3

{{ cookiecutter.license_py }}

import copy
import pathlib

import setuptools
from setuptools.command.build_py import build_py

NAME = 'reforis_{{cookiecutter.plugin_name_snake}}'

BASE_DIR = pathlib.Path(__file__).absolute().parent


class {{cookiecutter.plugin_name_camel}}Build(build_py):
    def run(self):
        # build package
        build_py.run(self)

        from reforis_distutils import ForisPluginBuild
        cmd = ForisPluginBuild(copy.copy(self.distribution))
        cmd.root_path = BASE_DIR
        cmd.module_name = NAME
        cmd.build_lib = self.build_lib
        cmd.ensure_finalized()
        cmd.run()


setuptools.setup(
    name=NAME,
    version='{{cookiecutter.version}}',
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,

    description='{{cookiecutter.description}}',
    author='CZ.NIC, z.s.p.o.',
    author_email='software@turris.com',

    install_requires=[
        'flask',
        'Babel',
        'Flask-Babel',
    ],
    extras_require={
        'devel': [
            'pytest',
            'pylint',
            'pylint-quotes',
            'pycodestyle',
            'reforis @ git+https://gitlab.nic.cz/turris/reforis/reforis#egg=reforis',
        ],
    },
    setup_requires=[
        'reforis_distutils',
    ],
    dependency_links=[
        'git+https://gitlab.nic.cz/turris/reforis/reforis-distutils.git#egg=reforis-distutils',
    ],
    entry_points={
        'foris.plugins': f'{NAME} = {NAME}:{{cookiecutter.plugin_name_snake}}'
    },
    classifiers=[
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    cmdclass={
        'build_py': {{cookiecutter.plugin_name_camel}}Build,
    },
    zip_safe=False,
)
