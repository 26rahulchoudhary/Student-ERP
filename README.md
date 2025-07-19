# College ERP System – Backend

A backend **College ERP System** built using **Django**, **Django REST Framework**, and **MySQL**, designed to manage students, faculty, courses, attendance, and academic results through RESTful APIs.

## Features

* Role-based User Management (Admin, Faculty, Student)
* Student & Faculty Management (CRUD APIs)
* Course Management & Enrollment
* Attendance Tracking and Reporting
* Marks Entry and Result Generation
* Django Admin Dashboard for Centralized Management
* REST APIs for Web or Mobile Integration

## Technologies Used

* Python
* Django
* Django REST Framework
* MySQL
* Git (Version Control)

## Setup Instructions

**Prerequisites:**

* Python 3.x
* pip package manager
* MySQL Server

**Steps:**

```bash
# Clone the repository
git clone https://github.com/your-username/college-erp-backend.git

# Navigate to project directory
cd college-erp-backend

# Install dependencies
pip install -r requirements.txt

# Configure MySQL database in settings.py

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver
```

Access API endpoints at: `http://127.0.0.1:8000/api/`

## Project Structure

* `manage.py` – Django management script
* `core/` – Project settings and configurations
* `apps/` – Custom apps (students, faculty, courses, attendance, results)
* `api/` – Django REST Framework-based API implementation
* `templates/` – HTML templates (if any)
* `static/` – Static files (optional)

## License

This project is open-source and created for academic and educational purposes.

---
