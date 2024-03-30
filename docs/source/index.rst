GraphQL API Gateway
===================

Пример реализации GraphQL API шлюза для взаимодействия с микросервисами.

Зависимости
===========

Установите требуемое ПО:

1. Docker для контейнеризации – |link_docker|

.. |link_docker| raw:: html

   <a href="https://www.docker.com" target="_blank">Docker Desktop</a>

2. Для работы с системой контроля версий – |link_git|

.. |link_git| raw:: html

   <a href="https://github.com/git-guides/install-git" target="_blank">Git</a>

3. IDE для работы с исходным кодом – |link_pycharm|

.. |link_pycharm| raw:: html

    <a href="https://www.jetbrains.com/ru-ru/pycharm/download" target="_blank">PyCharm</a>


Установка
=========

1. Клонируйте репозиторий проекта в свою рабочую директорию:

    .. code-block:: console

        git clone https://github.com/ctpemho7/python-course-graphql-gateway-example.git

Перед началом использования приложения необходимо его сконфигурировать.

.. note::

    Для конфигурации выполните команды, описанные ниже, находясь в корневой директории проекта (на уровне с директорией `src`).

2. Скопируйте файл настроек `.env.sample`, создав файл `.env`:
    .. code-block:: console

        cp .env.sample .env

    Этот файл содержит преднастроенные переменные окружения, значения которых будут общими для всего приложения.
    Файл примера (`.env.sample`) содержит набор переменных со значениями по умолчанию.
    Созданный файл `.env` можно настроить в зависимости от окружения.

    .. warning::

        Никогда не добавляйте в систему контроля версий заполненный файл `.env` для предотвращения компрометации информации о конфигурации приложения.

3. Соберите Docker-контейнер с помощью Docker Compose:
    .. code-block:: console

        docker compose build

    Данную команду необходимо выполнять повторно в случае обновления зависимостей в файле `requirements.txt`.

4. После сборки контейнеров можно их запустить командой:
    .. code-block:: console

        docker compose up

    Данная команда запустит собранные контейнеры для приложения и базы данных.
    Когда запуск завершится, сервер начнет работать по адресу `http://127.0.0.1:8000`.



Использование
=============

Запросы
-------
Этот проект предоставляет фикстуры для тестирования GraphQL. Фикстуры расположены в `src/fixtures`.
В них содержатся JSON-файлы для информации о любимых местах и странах.
GraphQL-приложение использует эти фикстуры для эмуляции ответов REST API.

Пример запроса на получение списка любимых мест:

.. code-block:: graphql

    query {
      places {
        latitude
        longitude
        description
        city
        locality
      }
    }

Пример запроса на получение списка любимых мест с информацией о странах:

.. code-block:: graphql

    query {
      places {
        latitude
        longitude
        description
        city
        locality
        country {
          name
          capital
          alpha2code
          alpha3code
          capital
          region
          subregion
          population
          latitude
          longitude
          demonym
          area
          numericCode
          flag
          currencies
          languages
        }
      }
    }

Этот запрос запросит дополнительную информацию о связанных странах оптимальным способом, используя загрузчики данных, чтобы предотвратить проблему N + 1 запросов.

Автоматизация
=============

Проект содержит специальный файл (`Makefile`) для автоматизации выполнения команд:

1. Сборка Docker-контейнера.
2. Генерация документации.
3. Запуск форматирования кода.
4. Запуск статического анализа кода (выявление ошибок типов и форматирования кода).
5. Запуск автоматических тестов.
6. Запуск всех функций поддержки качества кода (форматирование, линтеры, автотесты).

Инструкция по запуску этих команд находится в файле `README.md`.


Тестирование
============


Для запуска автоматических тестов выполните команду:

.. code-block:: console

    make test

Отчет о тестировании находится в файле `src/htmlcov/index.html`.


Документация к исходному коду
=============================

Сервисный слой
==============

Сервис для стран
----------------
.. automodule:: services.countries
    :members:

Сервис для новостей
-------------------
.. automodule:: services.news
    :members:

Сервис для мест
---------------
.. automodule:: services.places
    :members:

Модели
======

Миксин
------
.. automodule:: models.mixins
    :members:

Модель для стран
----------------
.. automodule:: models.countries
    :members:

Модель для новостей
-------------------
.. automodule:: models.news
    :members:

Модель для мест
---------------
.. automodule:: models.places
    :members: