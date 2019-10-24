#  Copyright (C) 2019 CZ.NIC z.s.p.o. (http://www.nic.cz/)
#
#  This is free software, licensed under the GNU General Public License v3.
#  See /LICENSE for more information.

.PHONY: prepare_template test lint init-langs

prepare_template:
	sh prepare_template.sh

test: prepare_template
	make -C reforis-example-plugin test

lint: prepare_template
	make -C reforis-example-plugin lint

init-langs: prepare_template
	make -C reforis-example-plugin init-langs