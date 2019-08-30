#  Copyright (C) 2019 CZ.NIC z.s.p.o. (http://www.nic.cz/)
#
#  This is free software, licensed under the GNU General Public License v3.
#  See /LICENSE for more information.

# !/usr/bin/env python3

import setuptools

setuptools.setup(
    name='reforis_{{cookiecutter.plugin_name_snake}}',
    version='{{cookiecutter.version}}',
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,

    description='{{cookiecutter.description}}',
    author='Bogdan Bodnar',

    # All versions are fixed just for case. Once in while try to check for new versions.
    install_requires=[
        'flask==1.0.2',
        'wtforms==2.2.1',
        'Flask-WTF==0.14.2',
        'Bootstrap-Flask==1.0.8',
    ],
    entry_points={
        'foris.plugins': '{{cookiecutter.plugin_name_snake}} = reforis_diagnostics:{{cookiecutter.plugin_name_snake}}'
    },
    classifiers=[
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    zip_safe=False,
)
