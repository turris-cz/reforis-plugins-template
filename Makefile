#  Copyright (C) 2020-2023 CZ.NIC z.s.p.o. (https://www.nic.cz/)
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

update-messages: prepare_template
	make -C reforis-example-plugin update-messages
