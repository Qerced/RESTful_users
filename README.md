# RESTful API мессенджера

## Тестовое задание "IT Workin"

<details open>
  <summary>Оглавление</summary>
  <ul>
    <li><a href="#описание">Описание</a></li>
    <li><a href="#настройка">Настройка</a></li>
    <li><a href="#запуск">Запуск</a></li>
    <li><a href="#требования">Требования</a></li>
  </ul>
</details>

## [Описание](#описание)

RESTful API для мессенджера обеспечивает взаимодействие через стандартные HTTP-запросы. API предоставляет возможность управления пользователями и обмена сообщениями.

## [Настройка](#настройка)

Шаблон заполнения `.env`:

```dotenv
debug=false
app_title=RESTful_users
secret=SECRET
db_host=mongodb
db_port=27017
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=admin
```

## [Запуск](#запуск)

Запустите сервис и его инфраструктуру командой:

```
docker-compose -f infra/docker-compose.yml up -d
```

## [Требования](#требования)

- [x] Механизм авторизации
- [x] Поиск пользователей
- [x] Возможность отправлять личные сообщения
- [x] Настройки пользователя (username, аватар, номер телефона, т.п.)
