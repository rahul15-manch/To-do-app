# To-Do List App 📝

A simple and efficient To-Do List web application built with Flask and SQLAlchemy, allowing users to manage tasks easily. Perfect for daily task tracking and productivity improvement.

## Features

- ✅ Add, update, and delete tasks

- ✅ Mark tasks as complete or pending

- ✅ Persist tasks in a SQL database

- ✅ RESTful routes for CRUD operations

- ✅ Deployable with Gunicorn for production

## Tech Stack

**Backend Framework:**  
![Flask](https://img.shields.io/badge/Flask-FFFFFF?style=for-the-badge&logo=flask&logoColor=000000)

**Database ORM:**  
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-000000?style=for-the-badge&logo=sqlalchemy&logoColor=FFFFFF) ![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-FF6F61?style=for-the-badge)

**Server:**  
![Gunicorn](https://img.shields.io/badge/Gunicorn-2C3E50?style=for-the-badge)

**Templating Engine:**  
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge)

**Utility Libraries:**  
![Blinker](https://img.shields.io/badge/Blinker-FF69B4?style=for-the-badge)  ![Click](https://img.shields.io/badge/Click-FF9900?style=for-the-badge)  ![importlib_metadata](https://img.shields.io/badge/importlib__metadata-4B0082?style=for-the-badge)  ![itsdangerous](https://img.shields.io/badge/itsdangerous-DC143C?style=for-the-badge)  ![MarkupSafe](https://img.shields.io/badge/MarkupSafe-32CD32?style=for-the-badge)  ![packaging](https://img.shields.io/badge/packaging-8A2BE2?style=for-the-badge)  ![typing_extensions](https://img.shields.io/badge/typing__extensions-FF4500?style=for-the-badge)  ![Werkzeug](https://img.shields.io/badge/Werkzeug-4682B4?style=for-the-badge)  ![zipp](https://img.shields.io/badge/zipp-20B2AA?style=for-the-badge)

## Installation

- Clone the repository
```
git clone https://github.com/yourusername/todo-flask-app.git
cd todo-flask-app
```

- Create a virtual environment
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

- Install dependencies
```
pip install -r requirements.txt
```

- Set up the database
```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
- Running the App
 - Development Mode
```
flask run


Visit http://127.0.0.1:5000

Production Mode (Gunicorn)
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Project Structure
```
todo-flask-app/
│
├── app/ # Main application package
│ ├── routes/ # Route handlers (Blueprints)
│ │ ├── init.py
│ │ ├── auth.py # Authentication routes
│ │ └── tasks.py # Task management routes
│ │
│ ├── static/ # Static assets (CSS, JS, images)
│ │ └── style.css
│ │
│ ├── templates/ # Jinja2 HTML templates
│ │ ├── base.html
│ │ ├── login.html
│ │ ├── register.html
│ │ └── tasks.html
│ │
│ ├── init.py # Flask app factory
│ └── models.py # Database models
│── instance/
  ├── site.db
│── run.py
│── .gitignore
├── Procfile # Deployment (Gunicorn entrypoint)
├── requirements.txt # Project dependencies
└── README.md # Documentation
```
## Author

👤 **Rahul Manchanda**  

- GitHub: [rahul15-manch](https://github.com/rahul15-manch)  
- LinkedIn: [Rahul Manchanda](https://www.linkedin.com/in/rahul-manchanda-3959b120a/)  
- Instagram: [@rahulmanchanda015](https://www.instagram.com/rahulmanchanda015/?__pwa=1)  

Feel free to connect for collaboration, feedback, or project discussions! 🚀
