# 🚀 Task Manager Web App - Profesyonel Sürüm

> **Proje Hakkında / Yazarın Notu:**
> *Bu projenin temelleri, core mantığı ve ana çalışma prensipleri **benim tarafımdan** yazılmıştır. Daha sonra, "Bu sistemi profesyonel bir endüstri standardına taşı!" diyerek gelişmiş bir Yapay Zeka ajanı ile eş-programlama (pair-programming) yaptım. Yapay zeka, kod kalitesini, veritabanı güvenliğini, gelişmiş oturum (session) yönetimini ve modern UI/UX tasarım standartlarını projeye entegre ederek bu mükemmel profesyonel readme dosyasını ve son ürünü ortaya çıkardı.*

## 📌 Proje Özeti
Task Manager Pro, kullanıcıların kişisel görevlerini güvenli bir şekilde oluşturabildiği, durumlarına (todo, in_progress, done) göre listeleyip takip edebildiği Full-Stack bir web uygulamasıdır. Klasik todo-app mantığının ötesine geçerek tamamen asenkron iletişim ağlarına, şifre kriptolama (password hashing) mimarilerine ve RESTful API yapılarına sahiptir.

## 🛠 Mimari ve Kullanılan Teknolojiler

### Backend (Sunucu ve Mantık Katmanı)
- **Framework:** Python / Flask
- **Veritabanı ORM:** Flask-SQLAlchemy (Otomatize veritabanı ilişkileri ve Cascade Delete)
- **Veritabanı:** SQLite3
- **Oturum ve Güvenlik:** Flask-Login (Session Persistence, `@login_required` middleware)
- **Kriptoloji:** Werkzeug Security (Güçlü Parola Hashleme - `pbkdf2:sha256`)

### Frontend (Kullanıcı İşlem Katmanı)
- **Tasarım Dili:** HTML5 ve Modern CSS3 (Flexbox, CSS Variables, Glassmorphism tarzı estetik modern tasarım)
- **Asenkron Veri Akışı:** Vanilla JavaScript (Fetch API - Sayfa yenilenmeksizin Single Page Application - SPA hissiyatı)

## 🚀 Öne Çıkan Profesyonel Özellikler

1. **Güvenli Kimlik Doğrulama (Auth System):** 
   - Parolalar veritabanına ASLA düz metin (plain-text) olarak kaydedilmez. Hashlenerek saklanır.
   - Tanımsız (Unauthorized) girişler Backend tarafından middleware ile engellenir.
2. **RESTful API Yaklaşımı:**
   - Frontend ve Backend tamamen bağımsız diller konuşur ve bilgiler `JSON` formatında `/api/` endpointleri aracılığı ile güvenle aktarılır.
3. **Akıllı Veritabanı İlişkileri (Foreign Key & Relational Database):**
   - Her `Task` (Görev) belirli bir `User` (Kullanıcı) ID'sine zimmetlenir. Bir kullanıcı başka bir kullanıcının görevlerini okuyamaz, değiştiremez veya silemez.
4. **Responsive (Duyarlı) ve Esnek Tasarım:**
   - Uygulama renk paletleri ve modern tasarım trendleri ile akıcı (fluid) bir deneyim sunar.

## ⚙️ Kurulum ve Çalıştırma

Bilgisayarınıza projeyi çekip yerel cihazınızda (localhost) çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

1. **Gerekli Kütüphaneleri Kurun:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Veritabanı Başlatma ve Uygulamayı Çalıştırma:**
   ```bash
   python app.py
   ```

3. **Erişim:**
   Tarayıcınızı açın ve aşağıdaki adrese gidin:
   `http://127.0.0.1:5000`

---
*Bu sistem geliştirilmeye devam edilmektedir ve açık kaynaklı kodlama standartlarına uygun olarak inşa edilmiştir.*
