all:

.PHONY: flake8 test translatable_strings update_translations docs

flake8:
	flake8 django_buzz tests

test:
	DJANGO_SETTINGS_MODULE=tests.settings PYTHONPATH=. \
		django-admin.py test tests

coverage:
	coverage erase
	DJANGO_SETTINGS_MODULE=tests.settings PYTHONPATH=. \
		coverage run --branch --source=django_buzz `which django-admin.py` test tests
	coverage html

translatable_strings:
	cd django_buzz && django-admin.py makemessages -l en --no-wrap --no-obsolete
	@echo "Please commit changes and run 'tx push -s' (or wait for Transifex to pick them)"

update_translations:
	tx pull
	cd django_buzz && django-admin.py compilemessages

docs:
	cd docs && make html