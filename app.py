#!/bin/python

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import click


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False)


@app.cli.command("init-db")
def init_db_command():
    """Clear existing data and create new tables."""
    with app.app_context():
        db.create_all()
    click.echo("Initialized the database.")


@app.route("/")
def home():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text")
    new_todo = Todo(text=text)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/update", methods=["POST"])
def update():
    todoId = int(request.form.get("todo_id"))
    todoToUpdate = Todo.query.get(todoId)

    if request.form.get("complete"):
        todoToUpdate.complete = True
    else:
        todoToUpdate.complete = False

    db.session.commit()
    return redirect(url_for("home"))


@app.route("/remove", methods=["POST"])
def remove():
    todoId = int(request.form.get("todo_id"))
    todoToRemove = Todo.query.get(todoId)
    db.session.delete(todoToRemove)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
