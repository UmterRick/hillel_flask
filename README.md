# Hillel Flask App

Міні-проєкт для управління студентами.
Реалізовано на Flask з використанням SQLAlchemy, Pydantic та HTML-шаблонів (Jinja2).

# Функціональність

- Перегляд списку студентів
- Додавання нового студента
- Пошук студентів за ім’ям (фронтенд)
- Виведення фото та назви курсу
- Автоматичний підрахунок віку (через Pydantic)
- Оновлення та видалення студентів через API
- Валідація даних на бекенді



Структура

flask_db_app/
├── .gitignore
├── run.py
├── pyproject.toml
├── poetry.lock
├── README.md
├── .env
├── instance/
│   └── db.sqlite
├── migrations/
│   └── versions/
│       ├── <міграції>
├── src/
│   └── flask_db_app/
│       ├── __init__.py
│       ├── config.py
│       ├── models.py
│       ├── schemas.py
│       ├── routes.py
│       └── templates/
│           └── students.html

Перевірка
- http://127.0.0.1:5000/students_ui — перегляд, додавання, пошук студентів через HTML-інтерфейс

- Використати Postman або curl для перевірки API:

- GET /students — отримати всіх студентів
- POST /add_student — додати нового студента
- PUT /update_student/<id> — оновити дані
- DELETE /delete_student/<id> — видалити студента
- GET /health — перевірка доступності сервера