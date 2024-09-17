# Django Project 
This project consists of two apps: 
1) christmasapp which answers the question: "is it christmas today?" 
2) secret_santa that allows users to add participants to the Secret Santa game, shuffle the participants, and assign each person a random recipient for gift-giving, ensuring no one is assigned themselves.

## How to start 
1) Clone the Repository
```` bash 
git clone https://github.com/imt17/web-2024.git
cd christmas
````
2) create virtual env
````bash
python -m venv venv
source venv/bin/activate
````
3) Install Dependencies
````bash
pip install -r requirements.txt
````
4) Apply Migrations
```bash
python manage.py migrate
```
5) Run the Development Server
```bash
python manage.py runserver

```