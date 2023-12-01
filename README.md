Обзор проекта
Добро пожаловать в наш проект на Django и Django Rest Framework (DRF)! Этот репозиторий служит основой для создания веб-приложения с использованием веб-фреймворка Django и расширения его возможностей с помощью Django Rest Framework для разработки API.

store-project/
│
├── api/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
│
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt

## Начало

1. git clone https://github.com/ваше-имя-пользователя/ваш-репо.git
2. python -m venv venv
3. Windows: .\venv\Scripts\activate     //      MacOS: .\venv\Scripts\activate
4. pip install -r requirements.txt
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py runserver

### Команды Django
- python manage.py makemigrations: создать миграции
- python manage.py migrate: применить миграции
- python manage.py test: запустить тесты
- python manage.py startapp app_name: запустить приложение


#### Благодарности
Документация Django
Документация Django Rest Framework

