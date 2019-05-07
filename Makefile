.PHONY = build FORCE
.DEFAULT_GOAL = build
VERSION = $(shell python -m setuptools_scm | cut -d" " -f3)

build: debian/changelog

debian/changelog: FORCE
	-rm -f debian/changelog
	dch --create --package "versada-odoo-backups" \
		--newversion $(VERSION) "release $(VERSION)"

FORCE:
