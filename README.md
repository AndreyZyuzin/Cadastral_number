[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

### Описание задания
1. Написать сервис, который принимает запрос с указанием кадастрового номера, широты и долготы, эмулирует отправку запроса на внешний сервер, который может обрабатывать запрос до 60 секунд. Затем должен отдавать результат запроса. Считается, что внешний сервер может ответить `true` или `false`.
2. Данные запроса на сервер и ответ с внешнего сервера должны быть сохранены в БД. Нужно написать АПИ для получения истории всех запросов/истории по кадастровому номеру.
3. Сервис должен содержать следующие эндпоинты:
"/query" - для получения запроса
“/result" - для отправки результата
"/ping" - проверка, что  сервер запустился
“/history” - для получения истории запросов
4. Добавить Админку.
5. Сервис завернуть в Dockerfile.
6. *В качестве дополнительного задания. Можно добавить дополнительный сервис, который будет принимать запросы первого сервиса и эмулировать внешний сервер.


### Запуск:


### Эндпоинты сервиса:
```
GET /query/ - для получения запроса
POST /result/ - для отправки результата
GET /ping/ - проверка, что  сервер запустился
GET /history/ - для получения истории запросов
```

### Автор:
Выполнено *Зюзиным Андреем* в качестве тестового задания.
