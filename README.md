# 🎓 Predictive Analytics for Student Performance in Online Courses

## 📌 Project Overview
This project is a Django-based web application integrated with Machine Learning to predict student performance in online courses. It analyzes factors such as attendance, marks, and activity data to generate predictions and insights.

The system helps educators identify at-risk students and improve learning outcomes through data-driven decisions.

---

## 🎯 Objectives
- Predict student performance using machine learning algorithms
- Develop a web interface for easy data input and result visualization
- Analyze academic data to provide meaningful insights
- Support better decision-making in online education systems

---

## 🚀 Features
- User Authentication (Login/Logout)
- Student Performance Prediction System
- Machine Learning Model Integration
- Admin Panel for data management
- CRUD Operations (Create, Read, Update, Delete)
- Dynamic result display using Django templates

---

## 🧠 Core Logic & Algorithms

### Machine Learning Model
- Algorithms Used:
  - Random Forest
  - Decision Tree
- Input Features:
  - Attendance
  - Marks
  - Activity Level
- Output:
  - Predicted Performance (Good / Average / Poor)

### Prediction Workflow
User Input → Data Preprocessing → Model Prediction → Result Display

### Authentication Flow
Input → Validate → Authenticate → Session Create → Dashboard

### CRUD Operations
- Create: Add new student data
- Read: Retrieve student records
- Update: Modify existing data
- Delete: Remove student records

### Request-Response Lifecycle
User Request → URL Routing → View → Model → Template → Response

---

## 🏗️ System Architecture
Frontend → Templates → Views → Machine Learning Model → Models → Database

---

## 🛠️ Tech Stack
- Backend: Python, Django
- Frontend: HTML, CSS, JavaScript
- Machine Learning: Scikit-learn
- Database: SQLite3

---

## 📂 Project Structure
project/
│── manage.py
│── db.sqlite3
├── admins/
├── project/

---

## ⚙️ Installation & Setup
1. git clone <your-repo-link>
2. cd project
3. python -m venv env
4. env\Scripts\activate
5. pip install django scikit-learn pandas numpy
6. python manage.py makemigrations
7. python manage.py migrate
8. python manage.py runserver

---

## 🔑 Admin Access
python manage.py createsuperuser

http://127.0.0.1:8000/admin/

---

## 🔐 Security
- CSRF Protection
- Password Hashing
- Session Authentication

---

## 📊 Database
SQLite (default)

---

## 📈 Example Output
Input: Attendance = 80%, Marks = 75, Activity = High  
Output: Predicted Performance = Good

---

## 📌 Future Improvements
- Deep Learning integration
- REST APIs
- React frontend
- Cloud deployment

---

## 👨‍💻 Author
Dhanush Anumalasetty
