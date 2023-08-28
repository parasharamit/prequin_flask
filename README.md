## Overview

* This project is about Flask based API services. Integration with Flask-restplus, Flask-Cors, Flask-Testing, Flask-SQLalchemy,and Flask-OAuth extensions.

### Extension:
- Restful: [Flask-restplus](http://flask-restplus.readthedocs.io/en/stable/)

- SQL ORM: [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

- Testing: [Flask-Testing](http://flask.pocoo.org/docs/0.12/testing/)

- OAuth: [Flask-OAuth](https://pythonhosted.org/Flask-OAuth/)


## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
.
|──────prequin_flask/
| |────__init__.py
| |────Configuration/
| | |────configreader.py
| | |────service.yml
| |────Scripts/
| | |────main.py
| | |────Constants/
| | | |────const.py
| | |────Services/
| | | |────__init__.py
| | | |────DatabaseConnection/
| | | | |────__init__.py
| | | | |────prequin_db_connection.py
| | | |────LoginRegister/
| | | | |────__init__.py
| | | | |────user_login.py
| | |────Utility
| | | |────Log
| | | | |────logger.py
| | | |────var
| |────README.md
| |────requirements.txt
| |────__root__.py
| |────run_flasked_api.py

```

**Objective:**
To develop RESTful APIs using that can be utilized by mobile and web applications. The applications will satisfy the following user stories:

● User should be able to login or sign up using his phone number (no OTP or verification code required).



**To run the project:**
Go to project directory and then run:


1) ``` python3 run_flasked_app.py ```
   
      OR
   
2) ``` gunicorn run_flasked_app:app_wsgi --preload -b 0.0.0.0:8000 ```


**Create new docker image for the project**

1) $ `docker build -t <container_image_name> <destination_dir>` 
      for e.g. `docker built -t truckbook-docker-image ./`

2) $ `docker image`s # To check running docker images

3) $ `docker run -rm -it -d -p <port_of_choice>:5011 <container_image_name>`



**Database**: 
Postgres (local)

**Descriptions of APIs and endpoints:**
1. Sign-up with phone number and password on sign-up page `0.0.0.0:8000/signup`
2. GET Method to fetch result GET `0.0.0.0:8000/`