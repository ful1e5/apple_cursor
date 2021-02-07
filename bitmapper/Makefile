all: install render

.PHONY: all

install: node_modules package.json 
	@yarn install 

render:
	@yarn render

watch:
	@yarn watch

node_modules:
	@mkdir -p $@

clean:
	@rm -rf node_modules yarn.lock