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
.ONESHELL:
SHELL:=/bin/bash
THEME_PREFIX = macOSBigSur

src := ./themes/

local := ~/.icons
local_dest := $(local)/$(theme)

root := /usr/share/icons
root_dest := $(root)/$(theme)


install: $(src)
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Installing '$(THEME_PREFIX)' cursors inside $(local)/..."
		@mkdir -p $(local)
		@cp -r ./themes/$(THEME_PREFIX) $(local_dest)
		@cp -r ./themes/$(THEME_PREFIX)-White $(local_dest) && echo "> Installed!"
	@else
		@echo "> Installing '$(THEME_PREFIX)' cursors inside $(root)/..."
		@mkdir -p $(root)
		@sudo cp -r ./themes/$(THEME_PREFIX) $(root_dest)
		@sudo cp -r ./themes/$(THEME_PREFIX)-White $(root_dest) && echo "> Installed!"
	@fi

uninstall:
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Removing '$(THEME_PREFIX)' from '$(local)'..."
		@rm -rf $(local)/$(THEME_PREFIX)
		@rm -rf $(local)/$(THEME_PREFIX)-White
	@else
		@echo "> Removing '$(THEME_PREFIX)' from '$(root)'..."
		@rm -rf $(root)/$(THEME_PREFIX)
		@rm -rf $(root)/$(THEME_PREFIX)-White
	@fi

reinstall: uninstall install


# generates binaries
BIN_DIR = ../bin
THEMES = White
prepare: bitmaps themes
	@rm -rf bin
	@mkdir -p bin/$(THEME_PREFIX)
	@$(foreach theme,$(THEMES), mkdir -p bin/$(THEME_PREFIX)-$(theme);)
	@cd bitmaps
	@zip -r $(BIN_DIR)/$(THEME_PREFIX)/bitmaps.zip $(THEME_PREFIX)
	@$(foreach theme,$(THEMES), zip -r $(BIN_DIR)/$(THEME_PREFIX)-$(theme)/bitmaps.zip $(THEME_PREFIX)-$(theme);)
	@zip -r $(BIN_DIR)/bitmaps.zip *
	@cd ..
	@cd themes
	@tar -czvf $(BIN_DIR)/$(THEME_PREFIX)/$(THEME_PREFIX).tar.gz $(THEME_PREFIX)
	@zip -r $(BIN_DIR)/$(THEME_PREFIX)/$(THEME_PREFIX)-Windows.zip $(THEME_PREFIX)-Windows
	@$(foreach theme,$(THEMES), tar -czvf $(BIN_DIR)/$(THEME_PREFIX)-$(theme)/$(THEME_PREFIX)-$(theme).tar.gz $(THEME_PREFIX)-$(theme);)
	@$(foreach theme,$(THEMES), zip -r $(BIN_DIR)/$(THEME_PREFIX)-$(theme)/$(THEME_PREFIX)-$(theme)-Windows.zip $(THEME_PREFIX)-$(theme)-Windows;)
	@cd ..
