# Todo App

A Flask-based todo app with SQLite for persistent task storage.
Built to learn backend development and database integration.

## Features

- Add, update, and delete tasks
- Mark tasks as complete/incomplete
- Persistent storage with SQLite

## Tech Stack

- Python 3.12
- Flask, Flask-SQLAlchemy
- SQLite
- Gunicorn (for production)
- Docker (optional deployment)

## Setup (Local)

1. Clone the repo: `git clone https://github.com/ARlynky/todo-webapp`
2. Install dependencies: `pip install -r requirements.txt` (venv is highly recommended)
3. Initialize database: `flask init-db`
4. Run: `flask run` (or `gunicorn --bind 0.0.0.0:5000 app:app` for production)
5. Visit the url something like: <http://localhost:5000>

## Setup (Docker)

1. Build: `docker build -t todo-app .`
2. Initialize database: `docker run --rm -it todo-app flask init-db`
3. Run: `docker run -d -p 5000:5000 --name todo-app todo-app`
4. Visit the url something like: <http://localhost:5000>

## Why I Built This

To practice Flask, SQLAlchemy, and Docker for backend and dev tooling skills.

## Future Plans

- Add user authentication (for online/multi user)
- Deploy to a VPS
