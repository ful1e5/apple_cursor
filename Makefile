all: clean render build

.PHONY: all

# Default
clean:
	@rm -rf bitmaps themes

render: bitmapper svg
	@cd bitmapper && make install render_bigsur render_monterey

build: bitmaps
	@cd builder && make setup build


# Specific platform build
unix: clean render bitmaps
	@cd builder && make setup build_unix

windows: clean render bitmaps
	@cd builder && make setup build_windows

# macOS Big Sur
bigsur: clean render_bigsur build_bigsur

render_bigsur: bitmapper svg
	@cd bitmapper && make install render_bigsur

build_bigsur: bitmaps
	@cd builder && make setup build_bigsur

# macOS Monterey
monterey: clean render_monterey build_monterey

render_monterey: bitmapper svg
	@cd bitmapper && make install render_monterey

build_monterey: bitmaps
	@cd builder && make setup build_monterey

# Installation
.ONESHELL:
SHELL:=/bin/bash
THEME_PREFIX = macOS

src := ./themes/

local := ~/.icons
local_dest := $(local)/$(theme)

root := /usr/share/icons
root_dest := $(root)/$(theme)


install: $(src)
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Installing '$(THEME_PREFIX)' cursors inside $(local)/..."
		@mkdir -p $(local)
		@cp -r ./themes/$(THEME_PREFIX)BigSur $(local_dest)
		@cp -r ./themes/$(THEME_PREFIX)BigSur-White $(local_dest)
		@cp -r ./themes/$(THEME_PREFIX)Monterey $(local_dest)
		@cp -r ./themes/$(THEME_PREFIX)Monterey-White $(local_dest) && echo "> Installed!"
	@else
		@echo "> Installing '$(THEME_PREFIX)' cursors inside $(root)/..."
		@mkdir -p $(root)
		@sudo cp -r ./themes/$(THEME_PREFIX)BigSur $(root_dest)
		@sudo cp -r ./themes/$(THEME_PREFIX)BigSur-White $(root_dest)
		@sudo cp -r ./themes/$(THEME_PREFIX)Monterey $(root_dest)
		@sudo cp -r ./themes/$(THEME_PREFIX)Monterey-White $(root_dest) && echo "> Installed!"
	@fi

uninstall:
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Removing '$(THEME_PREFIX)' from '$(local)'..."
		@rm -rf $(local)/$(THEME_PREFIX)BigSur
		@rm -rf $(local)/$(THEME_PREFIX)BigSur-White
		@rm -rf $(local)/$(THEME_PREFIX)Monterey
		@rm -rf $(local)/$(THEME_PREFIX)Monterey-White
	@else
		@echo "> Removing '$(THEME_PREFIX)' from '$(root)'..."
		@rm -rf $(root)/$(THEME_PREFIX)BigSur
		@rm -rf $(root)/$(THEME_PREFIX)BigSur-White
		@rm -rf $(root)/$(THEME_PREFIX)Monterey
		@rm -rf $(root)/$(THEME_PREFIX)Monterey-White
	@fi

reinstall: uninstall install


# generates binaries
BIN_DIR = ../bin
THEMES = White
prepare: bitmaps themes
	@rm -rf bin
	@mkdir -p bin/$(THEME_PREFIX)BigSur
	@$(foreach theme,$(THEMES), mkdir -p bin/$(THEME_PREFIX)BigSur-$(theme);)
	@mkdir -p bin/$(THEME_PREFIX)Monterey
	@$(foreach theme,$(THEMES), mkdir -p bin/$(THEME_PREFIX)Monterey-$(theme);)
	@cd bitmaps
	@zip -r $(BIN_DIR)/$(THEME_PREFIX)BigSur/bitmaps.zip $(THEME_PREFIX)BigSur
	@$(foreach theme,$(THEMES), zip -r $(BIN_DIR)/$(THEME_PREFIX)BigSur-$(theme)/bitmaps.zip $(THEME_PREFIX)BigSur-$(theme);)
	@zip -r $(BIN_DIR)/$(THEME_PREFIX)Monterey/bitmaps.zip $(THEME_PREFIX)Monterey
	@$(foreach theme,$(THEMES), zip -r $(BIN_DIR)/$(THEME_PREFIX)Monterey-$(theme)/bitmaps.zip $(THEME_PREFIX)Monterey-$(theme);)
	@zip -r $(BIN_DIR)/bitmaps.zip *
	@cd ..
	@cd themes
	@tar -czvf $(BIN_DIR)/$(THEME_PREFIX)BigSur/$(THEME_PREFIX)BigSur.tar.gz $(THEME_PREFIX)BigSur
	@zip -r $(BIN_DIR)/$(THEME_PREFIX)BigSur/$(THEME_PREFIX)BigSur-Windows.zip $(THEME_PREFIX)BigSur-Windows
	@tar -czvf $(BIN_DIR)/$(THEME_PREFIX)Monterey/$(THEME_PREFIX)Monterey.tar.gz $(THEME_PREFIX)Monterey
	@zip -r $(BIN_DIR)/$(THEME_PREFIX)Monterey/$(THEME_PREFIX)Monterey-Windows.zip $(THEME_PREFIX)Monterey-Windows
	@$(foreach theme,$(THEMES), tar -czvf $(BIN_DIR)/$(THEME_PREFIX)BigSur-$(theme)/$(THEME_PREFIX)BigSur-$(theme).tar.gz $(THEME_PREFIX)BigSur-$(theme);)
	@$(foreach theme,$(THEMES), zip -r $(BIN_DIR)/$(THEME_PREFIX)BigSur-$(theme)/$(THEME_PREFIX)BigSur-$(theme)-Windows.zip $(THEME_PREFIX)BigSur-$(theme)-Windows;)
	@$(foreach theme,$(THEMES), tar -czvf $(BIN_DIR)/$(THEME_PREFIX)Monterey-$(theme)/$(THEME_PREFIX)Monterey-$(theme).tar.gz $(THEME_PREFIX)Monterey-$(theme);)
	@$(foreach theme,$(THEMES), zip -r $(BIN_DIR)/$(THEME_PREFIX)Monterey-$(theme)/$(THEME_PREFIX)Monterey-$(theme)-Windows.zip $(THEME_PREFIX)Monterey-$(theme)-Windows;)
	@cd ..
