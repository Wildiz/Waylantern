.PHONY: install build check links
install:
	pip install pyyaml jsonschema
build:
	python3 scripts/build.py
check:
	python3 scripts/build.py --check
links:
	python3 scripts/check_links.py
