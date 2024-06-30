LOCATION := src
FLAKE_CONF := .flake8

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo ""
	@echo "Commands:"
	@echo "  lint                   Stop and remove containers"
	@echo "  fmt                    Start containers in the background"
	@echo "  help                   Display this help"
	@echo ""
	@echo "Usage:"
	@echo "  make [COMMAND]"
	@echo ""

.PHONY: lint
lint:
	poetry run flake8 --config $(FLAKE_CONF)

.PHONY: fmt
fmt:
	poetry run isort $(LOCATION)
	poetry run black $(LOCATION)