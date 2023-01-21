# Yatube_api

## RESTful API для проекта Yatube

> Yatube это социальная сеть, где каждый может поделиться постом,
оставить свой комментарий, подписаться на друга или  вступить в группу.

> Проект Yatube развивается, что стало результатом создания Yatube_api.
Через этот интерфейс смогут работать мобильное приложение или чат-бот;
через него же можно будет передавать данные в любое приложение или на фронтенд.

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Над проектом работали](#над-проектом-работали)

## Технологии
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)


### Использование:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Yana-Denisova/api_final_yatube.git
```

```
cd api_final_yatube
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

Документация к API в формате ReDoc доступна по адресу http://127.0.0.1:8000/redoc/ после запуска проекта


## Некоторые примеры запросов к API.


Получить список всех публикаций. При указании параметров limit и offset выдача работает с пагинацией.


``` 
GET /api/v1/posts/
```

RESPONSE:

```
{
    "count": 12,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=1&offset=3",
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=1&offset=1",
    "results": [
        {
            "id": 3,
            "author": "Yana",
            "text": "test text",
            "pub_date": "2022-02-10T13:37:56.728659Z",
            "image": null,
            "group": null
        }
    ]
}
```

Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.

```
POST /api/v1/posts/
```

REQUEST:

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Добавление нового комментария к публикации. Анонимные запросы запрещены.


```
POST /api/v1/posts/{post_id}/comments/
```

REQUEST:

```
{
  "text": "string"
}
```

Получение списка доступных сообществ.

```
GET /api/v1/groups/
```

RESPONSE:

```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```

## Над проектом работали

- [Денисова Яна](https://t.me/DenisovaYana)
