from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(20))
    deadline = db.Column(db.String(20))
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


@app.route("/")
def index():

    search = request.args.get("search")

    if search:
        tasks = Task.query.filter(Task.content.contains(search)).all()
    else:
        tasks = Task.query.order_by(Task.created_at.desc()).all()

    total = Task.query.count()
    completed = Task.query.filter_by(completed=True).count()

    percent = 0
    if total > 0:
        percent = int((completed / total) * 100)

    return render_template(
        "index.html",
        tasks=tasks,
        total=total,
        completed=completed,
        percent=percent
    )


@app.route("/add", methods=["POST"])
def add():

    content = request.form.get("task")
    priority = request.form.get("priority")
    deadline = request.form.get("deadline")

    if content:
        new_task = Task(
            content=content,
            priority=priority,
            deadline=deadline
        )

        db.session.add(new_task)
        db.session.commit()

    return redirect(url_for("index"))


@app.route("/complete/<int:id>")
def complete(id):

    task = Task.query.get_or_404(id)
    task.completed = not task.completed

    db.session.commit()

    return redirect(url_for("index"))


@app.route("/delete/<int:id>")
def delete(id):

    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)