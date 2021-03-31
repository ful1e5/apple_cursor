
all: clean setup build

.PHONY: all

.ONESHELL:
SHELL:=/bin/bash

X_SIZES ?=22 24 28 32 40 48 56 64 72 80 88 96
WIN_CANVAS_SIZE ?= 32
WIN_SIZE ?= 24

clean:
	@rm -rf applbuild.egg-info build dist
	@find -iname "*.pyc" -delete

	# Removing setup.py package files if installed
	@if [ -f "files.txt" ]; then
		@xargs rm -rf < files.txt
		@rm -rf files.txt
	@fi

setup: setup.py
	@python3 setup.py install --user --record files.txt

build: setup build.py
	@python3 build.py --xsizes $(X_SIZES) --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE)

build_unix: setup build.py
	@python3 build.py unix --xsizes $(X_SIZES)

build_windows: setup build.py
	@python3 build.py windows --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE)
