ENV = /usr/bin/env

.SHELLFLAGS = -c # Run commands in a -c flag
.SILENT: ; # no need for @
.ONESHELL: ; # recipes execute in same shell
.NOTPARALLEL: ; # wait for this target to finish
.EXPORT_ALL_VARIABLES: ; # send all vars to shell

.PHONY: all # All targets are accessible for user
.DEFAULT: help # Running Make will run the help target

help: ## Show Help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean:
	find . -iname '*.swp' -delete
	find . -iname '*.pyc' -delete
	find . -iname '*.pyo' -delete
	find . -iname '__pycache__' -delete
	rm -rf dist
	rm -f count.out
	rm -rf promotion.egg-info

security: ## Run security code checks
	echo "Running security check"
	bandit -r --ini .bandit

typping: ## Run static type checker
	echo "Running type check"
	mypy

lint: ## Run lint
	echo "Running linter check"
	pylint promotion

check: lint typping security ## Run pylint, mypy and bandit

test: ## Run tests
	pytest

install: ## Install system wide
	python setup.py install
