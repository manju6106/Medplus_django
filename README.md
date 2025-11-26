# MedCare Pharmacy – Django Web Application

## Overview
MedCare Pharmacy is a Django-based web application built to manage medicine information and streamline core pharmacy operations. It provides structured handling of medicine records, including storage of essential attributes such as medicine ID, name, cost, usage details, dosage, expiry date, and image uploads. The system uses Django’s MVT architecture to keep data access, business logic, and user interface layered and maintainable.

## Features
- Add new medicines with complete details  
- Store images securely through Django’s media handling  
- View all stored medicines in a structured layout  
- Edit and delete functionalities if configured in views  
- Full form validation and CSRF protection  
- Clean URL routing connected to dedicated views  
- Extendable architecture for future pharmacy modules

## Technologies Used
- Python 3  
- Django Framework  
- SQLite (default Django database)  
- HTML Templates  
- Django ORM  
- Bootstrap or basic CSS (if applied)

## Project Structure
Medplus_django/
│
├── Medplus/
│ ├── settings.py # Project settings and media configuration
│ ├── urls.py # Global URL routing
│ ├── wsgi.py
│ └── asgi.py
│
├── app_name/ # Replace with your Django app folder name
│ ├── migrations/
│ ├── templates/ # HTML files
│ ├── static/ # CSS/JS if included
│ ├── models.py # Medicine model
│ ├── views.py # Application logic
│ ├── urls.py # App URL routes
│ └── forms.py # Forms for medicine handling
│
├── media/ # Uploaded images
├── db.sqlite3 # Database file
├── manage.py
└── requirements.txt


## Installation and Setup
git clone https://github.com/manju6106/Medplus_django

cd Medplus_django
python -m venv venv
venv\Scripts\activate # Windows
pip install -r requirements.txt
python manage.py migrate


## Running the Project
python manage.py runserver

## Open the application at:
http://127.0.0.1:8000/


## Core Functionality
- Medicine details are submitted through an HTML form using the POST method.  
- Django views process the form, validate input, and store data via ORM.  
- Images are uploaded to dedicated media folders configured in `settings.py`.  
- Templates display stored medicines and their associated data.  
- URL routing ensures a clean path between actions like adding or viewing items.

## Key Files
- `models.py` – Defines the medicine data structure  
- `views.py` – Contains logic for handling requests  
- `forms.py` – Manages Django form creation  
- `templates/` – Holds the user interface pages  
- `urls.py` – Maps user actions to views  
- `settings.py` – Controls database, media, and static configurations  

## Future Enhancements
- Authentication system (Admin, Staff)  
- Inventory stock-level tracking  
- Billing system for sales  
- Medicine search and filtering  
- Expiry alerts and reporting  
- Improved UI design and responsiveness  

## Requirements
The project depends on the following Python packages:

Django
Pillow

Ensure these are included in `requirements.txt`.

## License
This project is free to use for learning and development. Add a formal license file if needed.


## License
Free to use for learning and development unless a specific license is added.


