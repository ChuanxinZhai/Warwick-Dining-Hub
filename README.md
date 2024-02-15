# Warwick-Dining-Hub
Warwick-Dining-Hub is an interactive hub for the University of Warwick’s dining facilities, providing view/add products, book a slot, submit feedback and search functions to students, staff and restaurant merchants. There are three main facilities in this website, the Beautiful Duck, StarBucks Cafe and Terrace Bar, which provide food, coffee and wine, respectively.

Dashboard Demo page as below: https://chuanxinzhai.github.io/Warwick-Dining-Hub/

If you want to see my other pages, you need to see my raw project because I didn't write the page jump logic code in html. I wrote the routes in app.py file.
![p](https://github.com/ChuanxinZhai/Warwick-Dining-Hub/assets/94314784/e0f729af-e12a-469b-b247-1030aeed4c66)


### Deploy guide
Download the folder: Warwick-Dining-Hub and unzip.

IDE: ![Visual Studio Code](https://img.shields.io/badge/-Visual%20Studio%20Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)


Install virtual python environment and Flask framework to your IDE.

Run **app.py** (if you don't want use my existing database, you need to run **add_inventory.py**, **booking.py**, **feedback.py** first, to initialize the database)

Open the local link: http://127.0.0.1:5000/

### Database ERD

![SQLite](https://img.shields.io/badge/-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)


![image](https://github.com/ChuanxinZhai/Warwick-Dining-Hub/assets/94314784/670a2f1d-61f4-4e01-8025-cbf99bd85e4c)


### Pytest
Open your command line terminal (cmd) as administrator.

Use cd method to enter the Warwick-Dining-Hub folder: cd C:\Users\your name\your path\Warwick-Dining-Hub

Use .\.venv\Scripts\Activate to enter the virtual environment.

Run the code below step by step to check the result.

- _python -m pytest tests/test_app.py_

- _python -m pytest tests/test_add_inventory.py_

- _python -m pytest tests/test_booking.py_

- _python -m pytest tests/test_feedback.py_

