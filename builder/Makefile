
all: setup build clean

.PHONY: all

clean:
	rm -rf applbuild.egg-info build dist
	find -iname "*.pyc" -delete

setup: clean setup.py
	test -d venv || virtualenv venv
	. venv/bin/activate; python3 setup.py install

build: setup build.py
	. venv/bin/activate; python3 build.py