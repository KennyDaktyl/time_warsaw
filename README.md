# Recruitment for "time" Warsaw

![N|Solid](https://www.grupazpr.pl/html/gfx/logo_welcome_v2.png)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Tech

Technologies used:

- [Python] - a programming language.
- [Django] - free and open-source web application development framework, written in Python
- [Django Restframework] - toolkit for building Web APIs.
- [PyTest] - framework for running automated Python tests.


## Installation

Download the source code from GitHub, install the virtual Python environment for the project, activate the environment then install external libraries for Django.

```sh
git clone https://github.com/KennyDaktyl/time_warsaw.git
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

The program gets SECRET_KEY from the system variable, so generate SECRET_KEY e.g.
https://miniwebtool.com/django-secret-key-generator/
```sh
export SECRET_KEY='3#$kwb#kuy2)c%u7j#p=h2jn)k6*t2=39kQt#_i7al$d9ih=%@'
```
starting the server
```sh
python3 manage.py runserver
```

Tests can be run from the console when the django server is running.
Go to the main application directory so that the tests.py file is visible
```sh
source env/bin/activate
pytest tests.py
```