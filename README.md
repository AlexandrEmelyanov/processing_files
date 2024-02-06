# Uploading and processing files - Сервис загрузки и обработки файлов

**Стек:**
+ [Python (Django Rest Framework)](https://www.python.org/downloads/)
+ [PostgreSQL](https://www.postgresql.org/)
+ [Redis](https://redis.io/)
+ [Celery](https://docs.celeryq.dev/en/stable/index.html#)
+ [Docker + docker-compose](https://www.docker.com/get-started/)


**Тестовое задание:** Необходимо разработать Django REST API, который позволяет загружать файлы на сервер, а затем 
асинхронно обрабатывать их с использованием Celery.

## Локальная разработка:

Все действия должны выполняться из исходного каталога проекта и только после установки всех требований.

1. Создайте и активируйте новую виртуальную среду:

```shell
python -m venv venv
venv\Scripts\activate
```

2. Склонируйте репозиторий с GitHub:

```shell
git clone <ссылка на репозиторий>
```

3. Установите пакеты:

```shell
pip install --upgrade pip
pip install -r requirements.txt
```

4. Выполните миграции в базу данных:

```shell
python manage.py migrate
```

5. Запустите Redis: [инструкция по запуску](https://redis.io/docs/install/install-redis/).


6. Запустите сервер:
```shell
python manage.py runserver
```

7. Запустите **Celery**:
   + если вы используете ОС Windows, необходимо запустить через **eventlet**:

    ```shell
    celery -A notification_service worker --loglevel=info -P eventlet
    ```

   + если другую ОС:

    ```shell
    celery -A store worker -l INFO
    ```

После успешного запуска, проект будет доступен по адресу: http://127.0.0.1:8000/ + реализованные endpoints
   
### Работа с API

Чтобы ознакомиться с описанием разработанного API, c доступными параметрами и примерами запросов после запуска проекта,
обратитесь к документации по адресу:
+ http://127.0.0.1:8000/docs/ - swagger документация
+ http://127.0.0.1:8000/redoc/ - redoc документация


### Админ-панель

Админ-панель доступна по адресу: http://127.0.0.1:8000/admin/ 

Вы можете посмотреть список добавленных файлов, также добавить новые.


### Тестовые данные

Вы можете загрузить файл фикстур, для заполнения данными БД.

```shell
python manage.py loaddata <path_to_fixture_files>
```

**Примечание 1:** файл фикстур в проекте находится по следующему пути:
+ files_api/fixtures/files.json

**Примечание 2:** после загрузки фикстур может потребоваться выполнить команды:

```shell
python manage.py makemigration 
python manage.py migrate
```

**Примечание 3:** если после загрузки фикстур в логах Celery возникают ошибки, очистите содержимое модели File и 
создайте новые.


## Запуск проекта с использованием docker-compose

После клонирования репозитория (см. п.1 и п.2 "Локальная разработка") перейдите в корневую папку проекта и выполните
команду:

```bash
docker-compose up --build
```

Эта команда соберет и запустит все необходимые контейнеры для проекта.

### После запуска выполните следующие команды:


1. Создайте суперпользователя:

```bash
docker-compose exec service python manage.py createsuperuser
```

После успешного запуска:

+ документация (swagger): http://127.0.0.1:8000/docs/


+ админ-панель: http://127.0.0.1:8000/admin/


+ проект будет доступен по адресу: http://127.0.0.1:8000/ + реализованные endpoints (см. п. Работа с API)

### Дополнительные команды

1. Для запуска в фоновом режиме:

```bash
docker-compose up -d --build
```

2. Для остановки контейнеров используйте:

```bash
docker-compose down
```

3. Для пересборки контейнеров и перезапуска проекта используйте:

```bash
docker-compose up --build
```

4. Для просмотра запущенных контейнеров:

```bash
docker ps
```