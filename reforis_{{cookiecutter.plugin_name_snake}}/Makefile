#  Copyright (C) 2019 CZ.NIC z.s.p.o. (http://www.nic.cz/)
#
#  This is free software, licensed under the GNU General Public License v3.
#  See /LICENSE for more information.

.PHONY: all prepare-dev install watch-js build-js lint lint-js lint-web test test-js test-web test-js-update-snapshots create-messages update-messages compile-messages clean

DEV_PYTHON=python3.7
ROUTER_PYTHON=python3.6

JS_DIR=./js

all:
	@echo "make lint"
	@echo "    Run list on project."
	@echo "make install"
	@echo "    Install package in your system (for running on router)."
	@echo "make build-js:"
	@echo "    Compile JS."
	@echo "make watch-js:"
	@echo "    Compile JS in watch mode."
	@echo "make create-messages"
	@echo "    Create locale messages (.pot)."
	@echo "make update-messages"
	@echo "    Update locale messages from .pot file."
	@echo "make compile-messages"
	@echo "    Compile locale messager."
	@echo "make clean"
	@echo "    Remove python artifacts and virtualenv."

prepare-dev:
	which npm || curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
	which npm || sudo apt install -y nodejs
	cd $(JS_DIR); npm install

install:
	$(ROUTER_PYTHON) -m pip install -e .
	ln -sf /tmp/reforis-diagnostics/reforis_static/{{cookiecutter.plugin_name_snake}} /tmp/reforis/reforis_static/

watch-js:
	cd $(JS_DIR); npm run-script watch
build-js:
	cd $(JS_DIR); npm run-script build

lint: lint-js lint-web
lint-js:
	cd $(JS_DIR); npm run lint
lint-web: venv
	$(VENV_BIN)/$(DEV_PYTHON) -m pylint --rcfile=pylintrc reforis
	$(VENV_BIN)/$(DEV_PYTHON) -m pycodestyle --config=pycodestyle reforis

test: test-js test-web
test-js:
	cd $(JS_DIR); npm test
test-web: venv
	$(VENV_BIN)/$(DEV_PYTHON) -m pytest -vv tests
test-js-update-snapshots:
	cd $(JS_DIR); npm test -- -u

create-messages:
	$(VENV_BIN)/pybabel extract -F babel.cfg -o ./reforis/translations/messages.pot .
update-messages:
	$(VENV_BIN)/pybabel update -i ./reforis/translations/messages.pot -d ./reforis/translations
	$(VENV_BIN)/pybabel update -i ./reforis/translations/tzinfo.pot -d ./reforis/translations -D tzinfo
compile-messages:
	$(VENV_BIN)/pybabel compile -f -d ./reforis/translations
	$(VENV_BIN)/pybabel compile -f -d ./reforis/translations -D tzinfo

clean:
	find . -name '*.pyc' -exec rm -f {} +
	rm -rf $(VENV_NAME) *.eggs *.egg-info dist build docs/_build .cache
	rm -rf dist build *.egg-info
	rm -rf $(JS_DIR)/node_modules/ reforis_static/{{cookiecutter.plugin_name_snake}}/app.min.js
	$(ROUTER_PYTHON) -m pip uninstall -y reforis_{{cookiecutter.plugin_name_snake}}
