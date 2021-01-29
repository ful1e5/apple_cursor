
all: clean setup build

.PHONY: all

.ONESHELL:
SHELL:=/bin/bash

clean:
	@rm -rf applbuild.egg-info build dist
	@find -iname "*.pyc" -delete

	# Removing setup.py package files if installed
	@if [ -f "files.txt" ]; then
		@xargs rm -rf < files.txt
		@rm -rf files.txt
	@fi

setup: setup.py
	@test -d venv || virtualenv venv
	@. venv/bin/activate; python3 setup.py install --record files.txt

build: setup build.py
	@. venv/bin/activate; python3 build.py

build_unix: setup build.py
	@. venv/bin/activate; python3 build.py unix

build_windows: setup build.py
	@. venv/bin/activate; python3 build.py windows