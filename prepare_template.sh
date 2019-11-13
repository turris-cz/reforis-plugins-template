#!/bin/bash

rm -rf reforis-example-plugin
python3 -m cookiecutter --no-input .
make -C reforis-example-plugin prepare-env
make -C reforis-example-plugin prepare-dev
