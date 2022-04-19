# Тестовое задание для Kvartirka.com

Задание: Реализовать REST API для системы комментариев блога.
------
**Функциональные требования:**
У системы должны быть методы API, которые обеспечивают

- Добавление статьи (Можно чисто номинально, как сущность, к которой крепятся комментарии).
- Добавление комментария к статье.
- Добавление коментария в ответ на другой комментарий (возможна любая вложенность).
- Получение всех комментариев к статье вплоть до 3 уровня вложенности.
- Получение всех вложенных комментариев для комментария 3 уровня.
- По ответу API комментариев можно воссоздать древовидную структуру.

**Нефункциональные требования:**

- Использование Django ORM.
- Следование принципам REST.
- Число запросов к базе данных не должно напрямую зависеть от количества комментариев, уровня вложенности.
- Решение в виде репозитория на Github, Gitlab или Bitbucket.
- readme, в котором указано, как собирать и запускать проект. Зависимости указать в requirements.txt либо использовать
  poetry/pipenv.
- Использование свежих версий python и Django.

**Будет плюсом:**

- Использование PostgreSQL.
- docker-compose для запуска api и базы данных.
- Swagger либо иная документация к апи.

<hr>

## Документация

Документация API была создана с помощью библиотеки `drf-yasg` и описана в формате Swagger/OpenAPI.
Файлы находятся в `kvartirka_api_test/docs/` в форматах **json** и **yaml**

<hr>

## Установка

```
pip3 install git
git clone https://github.com/joerude/kvartirka_api_test
cd kvartirka_api_test
```

Установите **poetry** для osx/linux/bash on windows:

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Для Windows powershell:

```
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

Затем запустите
```
poetry install
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py dump.json
python manage.py runserver
```

## Реализация
База данных: **PostgreSQL** <br>
Для реализации дерева комментариев использовалась структура 
данных MPTT (Modified Preorder Tree Traversal), а именно пакет `django-mptt`.


## Деплой
Ссылка: 
**https://joerude-test-comment-api.herokuapp.com/**



