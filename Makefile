all: clean render build install

.PHONY: all

clean:
	rm -rf pngs themes
	
render:
	cd bitmap && $(MAKE)

build:
	cd builder && $(MAKE)

SHELL:=/bin/bash
.ONESHELL:
install: themes/macOSBigSur
	if [[ $EUID -ne 0 ]]; then
		rm -rf ~/.icons/macOSBigSur
		cp -r themes/macOSBigSur ~/.icons/
	else
		sudo rm -rf /usr/share/icons/macOSBigSur
		sudo cp -r themes/macOSBigSur /usr/share/icons/
	fi


uninstall:
	if [[ $EUID -ne 0 ]]; then
		rm -rf ~/.icons/macOSBigSur
	else
		sudo rm -rf /usr/share/icons/macOSBigSur
	fi

