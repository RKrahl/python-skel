PYTHON = python3


build:
	$(PYTHON) setup.py build

test:
	$(PYTHON) setup.py test

sdist:
	$(PYTHON) setup.py sdist

doc-html: init_py
	$(MAKE) -C doc html

doc-pdf: init_py
	$(MAKE) -C doc latexpdf

clean:
	rm -rf build

distclean: clean
	rm -f MANIFEST .version
	rm -f $distname/__init__.py
	rm -rf dist
	$(MAKE) -C doc distclean

init_py:
	$(PYTHON) setup.py init_py


.PHONY: build test sdist clean distclean init_py
