# 📝 TaskFlow — Modern Task Manager

[English](#english) | [Türkçe](#türkçe)

---

<a name="english"></a>
## 🇬🇧 English

### About the Project

TaskFlow is a full-stack task management web application featuring a modern Kanban-style interface. Built with Flask and SQLAlchemy, it provides user authentication, task organization, search and filtering, and progress tracking through a clean, responsive UI.

### Key Features

- **User Authentication:** User registration and login with Flask-Login and secure password hashing.
- **Kanban Board:** Organize tasks into three statuses: To Do, In Progress, and Done.
- **Progress Tracking:** Visualize task completion with a dynamic progress bar.
- **Task Search:** Search and filter tasks based on their content.
- **Responsive UI:** A modern glassmorphism-inspired interface with dark and light themes.

### Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-Login
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **Database:** SQLite
- **Configuration & Security:** python-dotenv, Werkzeug

### Quick Start

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ismail7eren-tech/task-manager-web.git
   cd task-manager-web
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   ```

   Windows:

   ```bash
   venv\Scripts\activate
   ```

   macOS / Linux:

   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables** if required by the project.

5. **Run the application** using the entry point specified in the project.

---

<a name="türkçe"></a>
## 🇹🇷 Türkçe

### Proje Hakkında

TaskFlow, modern bir Kanban arayüzüne sahip full-stack görev yönetimi web uygulamasıdır. Flask ve SQLAlchemy ile geliştirilen uygulama; kullanıcı kimlik doğrulama, görev organizasyonu, arama ve filtreleme ile ilerleme takibi özellikleri sunar.

### Temel Özellikler

- **Kullanıcı Kimlik Doğrulama:** Flask-Login ve güvenli parola hashleme ile kayıt ve giriş sistemi.
- **Kanban Panosu:** Görevleri Yapılacak, Devam Ediyor ve Tamamlandı durumlarına göre düzenleme.
- **İlerleme Takibi:** Görev tamamlanma durumunu dinamik bir ilerleme çubuğuyla görüntüleme.
- **Görev Arama:** Görev içeriklerine göre arama ve filtreleme.
- **Duyarlı Arayüz:** Açık ve koyu tema seçeneklerine sahip modern glassmorphism tasarımı.

### Kullanılan Teknolojiler

- **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-Login
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **Veritabanı:** SQLite
- **Yapılandırma ve Güvenlik:** python-dotenv, Werkzeug

### Hızlı Başlangıç

Kurulum adımları için yukarıdaki İngilizce bölümde yer alan komutları takip edebilirsin.