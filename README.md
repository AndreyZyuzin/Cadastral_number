[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![celery](https://img.shields.io/badge/-celery-464646?style=flat-square&logo=celery)](https://docs.celeryq.dev/)
[![redis](https://img.shields.io/badge/-redis-464646?style=flat-square&logo=redis)](https://redis.io/)


### Описание задания
1. Написать сервис, который принимает запрос с указанием кадастрового номера, широты и долготы, эмулирует отправку запроса на внешний сервер, который может обрабатывать запрос до 60 секунд. Затем должен отдавать результат запроса. Считается, что внешний сервер может ответить `true` или `false`.
2. Данные запроса на сервер и ответ с внешнего сервера должны быть сохранены в БД. Нужно написать АПИ для получения истории всех запросов/истории по кадастровому номеру.
3. Сервис должен содержать следующие эндпоинты:\
"/query" - для получения запроса\
“/result" - для отправки результата\
"/ping" - проверка, что  сервер запустился\
“/history” - для получения истории запросов\
4. Добавить Админку.
5. Сервис завернуть в Dockerfile.
6. *В качестве дополнительного задания. Можно добавить дополнительный сервис, который будет принимать запросы первого сервиса и эмулировать внешний сервер.


### Запуск:
```
git clone git@github.com:AndreyZyuzin/Cadastral_number.git
cd Cadastral_number

python3 -m venv .venv
source venv/bin/activate
```

В main_service/settings.py необходимо поменять значение 
EXTERNAL_RESULT и EXTERNAL_PING

Главный сервер
```
python main_service/mangage.py migrate
python main_service/mangage.py createsuperuser
python main_service/mangage.py runserver
```


Установка Celery и Redis в другом терминале
```
python -m pip install celery

sudo apt update
sudo apt install redis

python -m pip install redis

python -m celery -A main_service worker
```

Внешний сервер в другом терминале
```
python main_service/mangage.py migrate 8001
python main_service/mangage.py createsuperuser
python main_service/mangage.py runserver
```

### Эндпоинты сервиса:

[http://localhost:8000/query/](http://localhost:8000/query/) - POST для получения запроса
[http://localhost:8000/result/<id>/](http://localhost:8000/result/1/) - GET для отправки результата
[http://localhost:8000/ping/](http://localhost:8000/ping/) - POST проверка, что  сервер запустился
[http://localhost:8000/history/](http://localhost:8000/history/) - GET для получения истории запросов


### Автор:
Выполнено **Зюзиным Андреем** в качестве тестового задания.
