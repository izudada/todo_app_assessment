#   Requirements

A app that keeps track of your to-do actions, you can add any number of tasks to it, search those tasks, click on the checkbox to complete the task, and filter using buttons like active tasks, completed tasks and all the tasks


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/izudada/todo_app_assessment.git
```

Create a virtual environment to install dependencies and activate it use the link below first to install pipenv:

https://pypi.org/project/pipenv/

then to activate a virtual enviroment:

```sh
$ pipenv shell
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```


Use migrate command to effect database model:

```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

Start the server with:
```sh
(folder_name)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`


### Useful resources

- [Medium](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f) - How to use environmental values
