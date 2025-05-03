# run.py

from src.flask_db_app import create_app  # імпортуємо фабрику додатку

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)