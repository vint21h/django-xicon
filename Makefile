# django-xicon
# Makefile


.ONESHELL:
PHONY: test help


test:
	./manage.py test $(TESTS)

help:
	@echo "    test:"
	@echo "        Run tests, can specify tests with 'TESTS' variable."
