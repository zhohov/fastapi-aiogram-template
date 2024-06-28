DC := docker-compose
DEV_COMPOSE := docker-compose.dev.yaml
PROD_COMPOSE := docker-compose.prod.yaml
env ?= dev

ifeq ($(env),dev)
    COMPOSE_FILE := $(DEV_COMPOSE)
else ifeq ($(env),prod)
    COMPOSE_FILE := $(PROD_COMPOSE)
else
    $(error Invalid value for env: $(env). Valid values are 'dev' or 'prod'.)
endif

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo ""
	@echo "Commands:"
	@echo "  build                  Build and start containers"
	@echo "  up                     Start containers in the background"
	@echo "  down                   Stop and remove containers"
	@echo "  exec var=<container>   Start an interactive shell in a container"
	@echo "  help                   Display this help"
	@echo ""
	@echo "Usage:"
	@echo "  make [COMMAND] env=<dev|prod>"
	@echo ""

.PHONY: build
build:
	$(DC) -f $(COMPOSE_FILE) up --build

.PHONY: up
up:
	$(DC) -f ${COMPOSE_FILE} up -d

.PHONY: down
down:
	$(DC) -f ${COMPOSE_FILE} down

.PHONY: exec
exec:
ifndef var
	$(error var is not set. Use 'make exec var=<container> env=<dev|prod>')
endif
	docker exec -it $(var) bash