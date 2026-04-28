# 🧾 Django Web Application

## 📌 Project Overview
This project is a Django-based web application developed to manage structured data efficiently with a secure backend and dynamic frontend. It follows Django’s MVT (Model-View-Template) architecture to ensure scalability and maintainability.

---

## 🎯 Objectives
- Build a scalable web application using Django
- Implement CRUD operations
- Ensure secure authentication system
- Provide responsive UI

---

## 🚀 Features
- User Authentication (Login/Logout)
- Admin Panel
- CRUD Operations
- Dynamic Templates
- SQLite Database Integration

---

## 🧠 Core Logic & Algorithms

### Authentication Flow
Input → Validate → Authenticate → Session Create → Dashboard

### CRUD Operations
- Create: Save data using `.save()`
- Read: Fetch using ORM `Model.objects.all()`
- Update: Modify and save object
- Delete: Remove using `.delete()`

### Request Lifecycle
User → URL → View → Model → Template → Response

---

## 🏗️ Architecture
Frontend → Templates → Views → Models → Database

---

## 🛠️ Tech Stack
- Python, Django
- HTML, CSS, JavaScript
- SQLite3

---

## 📂 Project Structure
project/
│── manage.py
│── db.sqlite3
├── admins/
├── project/

---

## ⚙️ Setup Instructions
1. git clone <repo>
2. cd project
3. python -m venv env
4. env\Scripts\activate
5. pip install django
6. python manage.py migrate
7. python manage.py runserver

---

## 🔐 Security
- CSRF Protection
- Password Hashing
- Session Authentication

---

## 📊 Database
SQLite (default)

---

## 📌 Future Improvements
- REST API
- React Frontend
- Deployment

---

## 👨‍💻 Author
Dhanush Anumalasetty
