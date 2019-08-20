# django-xicon
# Makefile


.ONESHELL:
PHONY: test help
NAME=xicon


test:
	pipenv run django-admin test --settings=$(NAME).tests.settings

help:
	@echo "    test:"
	@echo "        Run tests."
