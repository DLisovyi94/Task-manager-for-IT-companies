# Task Manager for IT Companies

This Django project is an internal system designed to manage tasks for development teams. It allows users to create tasks, assign them to team members, track progress, and organize teams and projects effectively.

## Check it out!

(You can add a deployed link here later.)

## Installing / Getting started

Python 3 must be already installed.

```shell
git clone https://github.com/your_username/task-manager-for-IT-companies.git
cd task-manager-for-IT-companies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env  # or create the .env file manually
python manage.py migrate
python manage.py runserver  # starts Django server
```

## Features
🔐 User authentication and login system

✅ Create, edit, assign and mark tasks as complete

👥 Team and project management

🏷 Tags for tasks (Many-to-Many)

📊 Track completed and pending tasks per worker

💼 Assign tasks to specific team members

🛠 Admin panel for advanced management

## Test User

For testing purposes, you can use the following credentials to log in:

Login: admin3
Password: 12345