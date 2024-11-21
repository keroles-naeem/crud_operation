# User Management System  

This project is a simple User Management System built with Django. It allows users to be created, viewed, updated, and deleted. The application is designed to provide a basic understanding of Django's model-view-template (MVT) architecture.  

## Features  

- User registration  
- User login and logout  
- View user profiles  
- Edit user details  
- Delete user accounts  
- List all users  

## Technologies Used  

- Python  
- Django  
- SQLite 
- HTML/CSS for front-end  
- Bootstrap 

## Getting Started  

These instructions will help you set up the project locally for development and testing purposes.  

### Prerequisites  

Make sure you have the following installed on your machine:  

- Python 3.6 or higher  
- pip (Python package manager)  
- virtualenv (optional but recommended)  

### Installation  

1. **Clone the repository:**  

   ```bash  
   git clone https://github.com/your-username/user-management-system.git  
   cd user-management-system
   ```
```bash
python -m venv venv  
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pipenv install
python manage.py migrate
python manage.py createsuperuser
```
2. **Run the development server:**
   ```bash
   python manage.py runserver

   ```
2. **Navigate:**
http://127.0.0.1:8000/users/
http://127.0.0.1:8000/users/create


