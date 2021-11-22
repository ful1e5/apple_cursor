all: setup build
.PHONY: all

.ONESHELL:
SHELL:=/bin/bash

bitmaps_dir = "../bitmaps"

X_SIZES ?=22 24 28 32 40 48 56 64 72 80 88 96
WIN_CANVAS_SIZE ?= 32
WIN_SIZE ?= 24

THEMES = White

setup:
	@python3 -m pip install clickgen --user

build: build_bigsur build_monterey
build_bigsur: build.py
	@python3 build.py -p "$(bitmaps_dir)/macOSBigSur" --xsizes $(X_SIZES) --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE)
	@$(foreach theme,$(THEMES), python3 build.py -p "$(bitmaps_dir)/macOSBigSur-$(theme)" --xsizes $(X_SIZES) --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE);)
build_monterey: build.py
	@python3 build.py -p "$(bitmaps_dir)/macOSMonterey" --xsizes $(X_SIZES) --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE)
	@$(foreach theme,$(THEMES), python3 build.py -p "$(bitmaps_dir)/macOSMonterey-$(theme)" --xsizes $(X_SIZES) --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE);)

build_unix: build_bigsur_unix build_monterey_unix
build_bigsur_unix: build.py
	@python3 build.py unix -p "$(bitmaps_dir)/macOSBigSur" --xsizes $(X_SIZES)
	@$(foreach theme,$(THEMES), python3 build.py unix -p "$(bitmaps_dir)/macOSBigSur-$(theme)" --xsizes $(X_SIZES);)
build_monterey_unix: build.py
	@python3 build.py unix -p "$(bitmaps_dir)/macOSMonterey" --xsizes $(X_SIZES)
	@$(foreach theme,$(THEMES), python3 build.py unix -p "$(bitmaps_dir)/macOSMonterey-$(theme)" --xsizes $(X_SIZES);)


build_windows: build_bigsur_windows build_monterey_windows
build_bigsur_windows: build.py
	@python3 build.py windows -p "$(bitmaps_dir)/macOSBigSur" --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE)
	@$(foreach theme,$(THEMES), python3 build.py windows -p "$(bitmaps_dir)/macOSBigSur-$(theme)" --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE);)
build_monterey_windows: build.py
	@python3 build.py windows -p "$(bitmaps_dir)/macOSMonterey" --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE)
	@$(foreach theme,$(THEMES), python3 build.py windows -p "$(bitmaps_dir)/macOSMonterey-$(theme)" --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE);)
