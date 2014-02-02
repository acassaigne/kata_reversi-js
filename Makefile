tests: install
	npm test

.ONESHELL:
ci:
	while true; do
		clear
		make tests
		inotifywait -q -e create,modify,delete *.js
	done

install:
	@[ -d node_modules ] || npm install
