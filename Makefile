test:
	./setup.py test

build: test
	./setup.py sdist

upload: test
	./setup.py sdist upload

clean:
	./setup.py clean
	rm -rf *.egg-info/
	rm -f MANIFEST nlbqx/*.pyc

distclean: clean
	rm -rf dist/

help:
	@echo "Usage: make <target>                   "
	@echo "                                       "
	@echo " test - run the tests                  "
	@echo " build - build the package             "
	@echo " upload - upload to PyPI               "
	@echo " clean - remove all build files        "
	@echo " distclean - remove all non git files  "
	@echo " help - show this help and exit        "
