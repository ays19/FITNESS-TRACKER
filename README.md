# 🏋️‍♂️ Fitness Tracker Web App

<p align="center">
  <img src="https://img.shields.io/badge/Django-Framework-green?style=for-the-badge&logo=django" />
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Status-Live-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Deployment-PythonAnywhere-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/ays19/FITNESS-TRACKER?style=for-the-badge" />
</p>

<p align="center">
  🚀 A full-stack Django web app to track workouts, monitor progress, and stay consistent with fitness goals.
</p>

---

## 🌐 Live Demo

👉 **[Click Here to View Live Project](https://ays19.pythonanywhere.com/)**

---

## 🎥 Project Preview

<p align="center">
  <img src="assets/demo.gif" alt="Fitness Tracker Demo" width="800"/>
</p>
---

## ✨ Features

✨ Clean & minimal user interface

🔐 Secure authentication system

📊 Track daily workouts & activities

✏️ Update and manage fitness records

❌ Delete records easily

📱 Responsive design (if added)

---

## 🧠 How It Works

mermaid
graph TD;
    A["User Signup/Login"] --> B["Dashboard"]
    B --> C["Add Workout"]
    B --> D["Update/Delete Records"]
    C --> E["Database (SQLite)"]
    D --> E
    E --> B


---

## 🛠️ Tech Stack

| Layer      | Technology     |
| ---------- | -------------- |
| Backend    | Python, Django |
| Frontend   | HTML, CSS      |
| Database   | SQLite         |
| Deployment | PythonAnywhere |

---

## 📂 Project Structure

```bash
FITNESS-TRACKER/
│── fitness_tracker/     # Main project settings
│── tracker_app/         # Core application logic
│── templates/           # HTML templates
│── static/              # CSS, JS, assets
│── assets/              # Screenshots & demo files
│── db.sqlite3
│── manage.py
```

---

## ⚙️ Installation Guide

### 🔹 1. Clone Repository

```bash
git clone https://github.com/ays19/FITNESS-TRACKER.git
cd FITNESS-TRACKER
```

### 🔹 2. Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 🔹 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 4. Run Migrations

```bash
python manage.py migrate
```

### 🔹 5. Start Server

```bash
python manage.py runserver
```

### 🔹 6. Open Browser

```
http://127.0.0.1:8000/
```

---

## 🎯 Key Learning Outcomes

✔️ Built a complete Django full-stack application
✔️ Implemented authentication system
✔️ Mastered CRUD operations
✔️ Learned deployment workflow
✔️ Improved project structuring skills

---

## 🚀 Future Improvements

* 📈 Add charts for progress tracking
* 🤖 AI-based fitness suggestions
* 📱 Fully responsive UI
* ☁️ Cloud database integration


---

## 👨‍💻 Author

**ays19**

🔗 GitHub: [https://github.com/ays19](https://github.com/ays19)
🌐 Live: [https://ays19.pythonanywhere.com/](https://ays19.pythonanywhere.com/)

---

## ⭐ Support

If this project helped or inspired you:

👉 Give it a **star ⭐**
👉 Share with others
👉 Follow for more projects
