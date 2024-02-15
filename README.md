# Warwick-Dining-Hub
Demo page: https://chuanxinzhai.github.io/Warwick-Dining-Hub/
![p](https://github.com/ChuanxinZhai/Warwick-Dining-Hub/assets/94314784/e0f729af-e12a-469b-b247-1030aeed4c66)


### Deploy guide
Download the folder: Warwick-Dining-Hub and unzip.

Install virtual python environment and Flask framework to your IDE.

Run app.py (if you don't want use my existing database, you need to run **add_inventory.py**, **booking.py**, **feedback.py** first)

Open the local link: http://127.0.0.1:5000/

### Pytest
Open your command line terminal (cmd) as administrator.

Use cd method to enter the Warwick-Dining-Hub folder: cd C:\Users\your name\your path\Warwick-Dining-Hub

Use .\.venv\Scripts\Activate to enter the virtual environment.

Run the code below step by step to check the result.

- _python -m pytest tests/test_app.py_

- _python -m pytest tests/test_add_inventory.py_

- _python -m pytest tests/test_booking.py_

- _python -m pytest tests/test_feedback.py_

