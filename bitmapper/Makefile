all: install render

.PHONY: all

clean:
	@find . -type f -name "yarn.lock" -exec rm -rf "{}" +;
	@find . -type d -name "node_modules" -exec rm -rf "{}" +;

node_modules:
	@mkdir -p $@

install: node_modules package.json
	@yarn install

render_bigsur:
	@yarn render:bigsur

render_monterey:
	@yarn render:monterey

render: render_bigsur render_monterey
