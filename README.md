# yamdb_final

## API для публикации постов с возможностью подписки на авторов.

### Примеры запросов:

your_host_ip - default 127.0.0.1:80
Регистрация:

```
POST http://{your_host_ip}/api/v1/auth/signup/
{
    "username": "myuser",
    "email": "test@test.test"
}
```

Получение токена

```
GET http://{your_host_ip}/api/v1/auth/token
{
    "username": "myuser",
    "confirmation_code": "code from mail"
}
```

Создание публикации:
```
POST http://{your_host_ip}/api/v1/posts/
```

Получить список всех произведений:
```
GET http:/{your_host_ip}/api/v1/titles/
```

Получение списка всех жанров:
```
GET http://{your_host_ip}/api/v1/genres/
```

Получение списка всех отзывов:

```
GET http://{your_host_ip}/api/v1/titles/{title_id}/reviews/
```
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/sokolovados/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Стэк:

Python 3.8<br>
Django 2.2<br>
Django Rest Framework 3.11<br>
DRF simplejwt 4.7<br>

### Автор

Вадим Соколов https://github.com/sokolovados
Максим Волочковский https://github.com/VarrySPb
Данил Воронин https://github.com/Bogdan-Malina

yamdb_final
![example workflow](https://github.com/github/docs/actions/workflows/main.yml/badge.svg)
