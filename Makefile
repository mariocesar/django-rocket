all:
	pip install -r requirements.txt

.PHONY: flake8
flake8:
	flake8 django_rocket tests

.PHONY: coverage
coverage:
	coverage erase
	DJANGO_SETTINGS_MODULE=tests.settings PYTHONPATH=. \
		coverage run --source=django_rocket `which django-admin.py` test tests
	coverage html

.PHONY: translatable_strings
translatable_strings:
	cd django_rocket && django-admin.py makemessages -l es --no-wrap --no-obsolete --keep-pot
	@echo "Please commit changes and run 'tx push -s' (or wait for Transifex to pick them)"

.PHONY: update_translations
update_translations:
	tx pull
	cd django_rocket && django-admin.py compilemessages

.PHONY: docs
docs:
	cd docs && make html