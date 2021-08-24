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
src := ./themes/

local := ~/.icons
local_dest := $(local)/$(theme)

root := /usr/share/icons
root_dest := $(root)/$(theme)

.ONESHELL:
SHELL:=/bin/bash


install: $(src)
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Installing 'macOSBigSur' cursors inside $(local)/..."
		@mkdir -p $(local)
		@cp -r ./themes/macOSBigSur $(local_dest)
		@cp -r ./themes/macOSBigSur-White $(local_dest) && echo "> Installed!"
	@else
		@echo "> Installing 'macOSBigSur' cursors inside $(root)/..."
		@mkdir -p $(root)
		@sudo cp -r ./themes/macOSBigSur $(root_dest)
		@sudo cp -r ./themes/macOSBigSur-White $(root_dest) && echo "> Installed!"
	@fi

uninstall:
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Removing 'macOSBigSur' from '$(local)'..."
		@rm -rf $(local)/macOSBigSur
		@rm -rf $(local)/macOSBigSur-White
	@else
		@echo "> Removing 'macOSBigSur' from '$(root)'..."
		@rm -rf $(root)/macOSBigSur
		@rm -rf $(root)/macOSBigSur-White
	@fi

reinstall: uninstall install

# generates binaries
BIN_DIR = ../bin
THEMES = White
prepare: bitmaps themes
	@rm -rf bin && mkdir bin
	@cd bitmaps && zip -r $(BIN_DIR)/bitmaps.zip * && cd ..
	@cd themes
	@tar -czvf $(BIN_DIR)/macOSBigSur.tar.gz macOSBigSur
	@zip -r $(BIN_DIR)/macOSBigSur-Windows.zip macOSBigSur-Windows
	@$(foreach theme,$(THEMES), tar -czvf $(BIN_DIR)/macOSBigSur-$(theme).tar.gz macOSBigSur-$(theme);)
	@$(foreach theme,$(THEMES), zip -r $(BIN_DIR)/macOSBigSur-$(theme)-Windows.zip macOSBigSur-$(theme)-Windows;)
	@cd ..
