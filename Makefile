theme := macOSBigSur
src := ./themes/$(theme)

local := ~/.icons
local_dest := $(local)/$(theme)

root := /usr/share/icons
root_dest := $(root)/$(theme)

all: clean render build

unix: clean render bitmaps
	@cd builder && make build_unix

windows: clean render bitmaps
	@cd builder && make build_windows

.PHONY: all

clean:
	@rm -rf bitmaps themes
	
render: bitmapper svg
	@cd bitmapper && $(MAKE)

build: bitmaps
	@cd builder && $(MAKE)

.ONESHELL:
SHELL:=/bin/bash


install: themes/macOSBigSur
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