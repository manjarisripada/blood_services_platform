# blood_services_platform
# Overview
This project is a web-based Blood Donation Management System designed to streamline the process of blood donation by categorizing users into roles with specific functionalities. Developed using the Django framework, this system provides a secure and user-friendly platform for managing blood donation requests, donor information, and blood stock levels, as well as allowing various users to interact with the system based on their assigned roles.

# Features
## User Roles and Functionalities
User Role:

Register and log in.
Explore information about blood donation.
Submit blood donation requests.
## Donor Role:

Update personal profiles.
View donation history.
Submit new blood donation requests, contributing to the overall blood stock.
## Staff Role:

Manage donor profiles.
Review and respond to donation requests.
Oversee and update blood stock levels.
## Medical Personnel Role:

Update profile information.
Review and approve donation requests based on medical criteria.
Provide medical descriptions or requirements for donation approvals.
# Technologies Used
## Django Framework:

Core framework for server-side logic and routing.
## HTML/CSS:

Used to design and style the user interface, ensuring a clean and responsive design.
## Python:

Backend logic and server-side scripting are implemented in Python, the primary language for this project.
## SQLite Database:

The default database system for Django, used here to store user data, donation records, and blood stock information.
## Bootstrap:

Used as the front-end framework for layout consistency, responsive design, and styling.
# Installation
Prerequisites
Python 3.x installed on your machine.
Django and other required libraries (use requirements.txt).
Steps
Clone the Repository:

bash
Copy code
git clone <repository_url>
Navigate to Project Directory:

bash
Copy code
cd blood-donation-management-system
Install Required Packages:

bash
Copy code
pip install -r requirements.txt
Run Migrations:

bash
Copy code
python manage.py migrate
Start the Server:

bash
Copy code
python manage.py runserver
Open your web browser and go to http://127.0.0.1:8000/ to access the system.

Usage
User Registration:

General users can register and log in to access the system.
Donors:

Can update their profiles and view donation history.
Submit donation requests, updating the blood stock levels accordingly.
Staff:

Manage and update donor profiles and respond to requests.
Medical Personnel:

Provide approval for donation requests and review donor medical information.
