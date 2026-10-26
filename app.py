import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

# .env dosyasındaki gizli ayarları çekiyoruz
load_dotenv()

app = Flask(__name__)

# Flask ve veritabanı ayarları
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default-fallback-key-for-dev")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///tasks.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Oturum (login/logout) işlemleri için
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Lütfen önce giriş yapın."

# ---  Buralar hep VERİTABANI TABLOLARI ---


# Kullanıcı tablosu
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

    # Kullanıcı silinirse görevleri de silinsin (cascade)
    tasks = db.relationship(
        "Task", backref="owner", lazy=True, cascade="all, delete-orphan"
    )

    # Editör (VS Code) class yapısını tanısın diye init ekledim
    def __init__(self, username: str, password_hash: str):
        self.username = username
        self.password_hash = password_hash


# Görev tablosu
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(20))
    deadline = db.Column(db.String(20))
    status = db.Column(db.String(20), default="todo")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    # Yine editörde hata altı çizilmesin diye init koydum
    def __init__(self, content, user_id, priority=None, deadline=None, status="todo"):
        self.content = content
        self.user_id = user_id
        self.priority = priority
        self.deadline = deadline
        self.status = status

    # API'ye veri yollarken JSON'a çevirmek için
    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "priority": self.priority,
            "deadline": self.deadline,
            "status": self.status,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }


# Sisteme giren kullanıcıyı hafızaya alıyor
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Tabloları oluştur (varsa es geçer)
with app.app_context():
    db.create_all()


# --- SAYFA YÖNLENDİRMELERİ ---


@app.route("/login", methods=["GET", "POST"])
def login():
    # Zaten giriş yapmışsa anasayfaya at
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    if request.method == "POST":
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()

        # Şifre kontrolü
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return jsonify({"success": True})

        return (
            jsonify({"success": False, "message": "Geçersiz kullanıcı adı veya şifre"}),
            401,
        )

    return render_template("login.html")


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # İsim alınmış mı bak
    if User.query.filter_by(username=username).first():
        return (
            jsonify({"success": False, "message": "Kullanıcı adı zaten alınmış"}),
            400,
        )

    new_user = User(username=username, password_hash=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)
    return jsonify({"success": True})


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/")
@login_required
def index():
    return render_template("index.html")


# --- API ENDPOINT'LERİ (Frontend için) ---


@app.route("/api/tasks")
@login_required
def get_tasks():
    search = request.args.get("search")
    query = Task.query.filter_by(user_id=current_user.id)

    # Arama yapıldıysa filtrele
    if search:
        query = query.filter(Task.content.contains(search))

    # En son eklenen en üste gelsin
    tasks = query.order_by(Task.created_at.desc()).all()

    # Basit istatistik hesapları
    total = len(tasks)
    completed = len([t for t in tasks if t.status == "done"])
    percent = int((completed / total) * 100) if total > 0 else 0

    return jsonify(
        {
            "tasks": [task.to_dict() for task in tasks],
            "stats": {"total": total, "completed": completed, "percent": percent},
        }
    )


@app.route("/api/add", methods=["POST"])
@login_required
def add():
    data = request.get_json()
    content = data.get("task")
    priority = data.get("priority", "Normal")
    deadline = data.get("deadline", "")

    # Boş görev eklenmesini engelle
    if content:
        new_task = Task(
            content=content,
            priority=priority,
            deadline=deadline,
            user_id=current_user.id,
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"success": True, "task": new_task.to_dict()})

    return jsonify({"success": False, "message": "Görev içeriği boş olamaz"}), 400


@app.route("/api/update_status/<int:id>", methods=["POST"])
@login_required
def update_status(id):
    # Başkasının görevini değiştiremesin diye filter_by'da user_id de var
    task = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    data = request.get_json()
    new_status = data.get("status")

    if new_status in ["todo", "in_progress", "done"]:
        task.status = new_status
        db.session.commit()
        return jsonify({"success": True, "task": task.to_dict()})

    return jsonify({"success": False, "message": "Geçersiz durum"}), 400


@app.route("/api/delete/<int:id>", methods=["DELETE"])
@login_required
def delete(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    return jsonify({"success": True})


if __name__ == "__main__":
    # .env dosyasından FLASK_DEBUG değerini okuyup ona göre başlatıyoruz
    app.run(debug=os.getenv("FLASK_DEBUG", "False").lower() == "true")
