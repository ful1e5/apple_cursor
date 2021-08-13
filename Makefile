all: clean render build
.PHONY: all

clean:
	@rm -rf bitmaps themes
	
render: bitmapper svg
	@cd bitmapper && $(MAKE)

build: bitmaps
	@cd builder && make build


unix: clean render bitmaps
	@cd builder && make build_unix

windows: clean render bitmaps
	@cd builder && make build_windows


# Installation
theme := macOSBigSur
src := ./themes/$(theme)

local := ~/.icons
local_dest := $(local)/$(theme)

root := /usr/share/icons
root_dest := $(root)/$(theme)

.ONESHELL:
SHELL:=/bin/bash

install: $(src)
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Installing '$(theme)' cursors inside $(local)/..."
		@mkdir -p $(local)
		@cp -r $(src) $(local_dest) && echo "> Installed!"
	@else
		@echo "> Installing '$(theme)' cursors inside $(root)/..."
		@mkdir -p $(root)
		@sudo cp -r $(src) $(root_dest) && echo "> Installed!"
	@fi

uninstall:
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Removing '$(local_dest)'..."
		@rm -rf $(local_dest)
	@else
		@echo "> Removing '$(root_dest)'..."
		@sudo rm -rf $(root_dest)
	@fi

reinstall: uninstall install

BIN_DIR = ../bin
prepare: bitmaps themes
	# Bitmaps
	@rm -rf bin && mkdir bin
	@cd bitmaps && zip -r $(BIN_DIR)/bitmaps.zip * && cd ..
	# Themes
	@cd themes
	@tar -czvf $(BIN_DIR)/macOSBigSur.tar.gz macOSBigSur
	@zip -r $(BIN_DIR)/macOSBigSur_Windows.zip macOSBigSur_Windows
	@cd ..
