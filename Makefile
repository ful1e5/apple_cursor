theme := macOSBigSur
src := ./themes/$(theme)

local := ~/.icons
local_dest := $(local)/$(theme)

root := /usr/share/icons
root_dest := $(root)/$(theme)

all: clean render build

unix: clean render pngs
	@cd builder && make build_unix

windows: clean render pngs
	@cd builder && make build_windows

.PHONY: all

clean:
	@rm -rf pngs themes
	
render: bitmap svg
	@cd bitmap && $(MAKE)

build: pngs
	@cd builder && $(MAKE)

.ONESHELL:
SHELL:=/bin/bash


install: themes/macOSBigSur
	@echo "> Installing '$(theme)' cursors..."
	@if [[ $EUID -ne 0 ]]; then
		@mkdir -p $(local)
		@cp -r $(src) $(local_dest) && echo "> Installed!"
	@else
		@mkdir -p $(root)
		@sudo cp -r $(src) $(root_dest) && echo "> Installed as root!"
	@fi

uninstall:
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Removing '$(local_dest)'..."
		@rm -rf $(local_dest)
	@else
		@echo "> Removing '$(root_dest)'..."
		@sudo rm -rf $(root_dest)
	@fi