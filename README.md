# fastapi-aiogram-template

Проект представляет собой шаблон для создания Телеграм ботов с использованием FastAPI для бэкенда. 
Шаблон включает возможность быстрого развертывания бота и бэкенда, а так же основных сервисов через docker compose, таких как:
* PostgreSQL, 
* Redis
* Nginx
* Certbot

## Оглавление

* [Настройка проекта](#set_up)
* [Запуск в режиме `dev`](#dev)
* [Запуск в режиме `prod`](#prod)


## Настройка проекта <a name="set_up"></a>

1. Клонировать репозиторий:
    ```bash
    git clone https://github.com/zhohov/fastapi-aiogram-template.git
    ```

2. Переименовать файл `.env` и заполнить его:
    ```bash
    mv .env.example .env
	  vim .env
    ```

## Запуск в режиме `dev` <a name="dev"></a>

1. Отредактировать конфигурацию Nginx, если запуск происходит не на локальной машине:
    ```bash
    vim nginx/dev/nginx.conf
    ```
    Замените `server_name 127.0.0.1;` на ваш домен или IP.

2. Запустить проект командой:
    ```bash
    make build
    ```
    или
    ```bash
    make build env=dev
    ```

## Запуск в режиме `prod` <a name="prod"></a>

1. Отредактировать конфигурацию Nginx для SSL:
    ```bash
    vim nginx/ssl/nginx.conf
    ```
    Замените `server_name domain.com;` на ваш домен.

2. Запустить проект для генерации SSL сертификата:
    ```bash
    make build env=ssl
    ```

3. После успешной генерации SSL сертификата, остановите контейнеры:
    ```bash
    make down
    ```

4. Отредактировать конфигурацию Nginx для продакшн:
    ```bash
    vim nginx/prod/nginx.conf
    ```
    Замените `server_name domain.com;` на ваш домен. Обновите пути к SSL сертификатам, заменив `domain.com` на ваш домен:
    ```nginx
    ssl_certificate /etc/letsencrypt/live/domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem;
    ```

5. Запустить проект:
    ```bash
    make build env=prod
    ```
