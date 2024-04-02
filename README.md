<div align="center">
  <h1>Task Manager</h1>
  <h3><a href="https://task-manager-pvjb.onrender.com/">A demo version of the application is available here</a></h3>

  [![hexlet-check](https://github.com/saintodes/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/saintodes/python-project-52/actions/workflows/hexlet-check.yml)
  [![python](https://github.com/saintodes/python-project-52/actions/workflows/lint-test.yml/badge.svg)](https://github.com/saintodes/python-project-52/actions/workflows/lint-test.yml)
  [![Maintainability](https://api.codeclimate.com/v1/badges/3d64b1f569bd495b3948/maintainability)](https://codeclimate.com/github/saintodes/python-project-52/maintainability)
<a href="https://codeclimate.com/github/saintodes/python-project-52/test_coverage"><img src="https://api.codeclimate.com/v1/badges/3d64b1f569bd495b3948/test_coverage" /></a>
</div>

<h2>Objective:</h2>
Task Manager is a web-based task management application, conceived as the capstone project for learners at Hexlet. This
project embodies the culmination of skills and knowledge acquired through the course, showcasing proficiency with
cutting-edge technologies, database design and interaction via ORM, automation of CRUD operations, custom form creation,
authentication and authorization mechanisms, data filtering libraries, and error tracking service integration.

<h2>Key Features:</h2>

User Registration and Authentication: Access to task creation, modification, and viewing is gated behind a user
registration and login system.
Task Creation: Users have the ability to create tasks, specifying details such as title, description, priority, status,
and assignee.
Task Status Modification: Users can update a task’s status (e.g., from "New" to "In Progress," "Completed," etc.) to
track its progress.
Assignee Specification: Tasks can be assigned to registered users, facilitating accountability and task delegation.
Task Filtering: Tasks can be filtered using forms based on various criteria (status, priority, assignee, etc.).
Authorization: Access control for task operations and user settings is managed through roles and permissions.
Error Tracking Service Integration: Error reports can be configured to be sent to services like Rollbar for real-time
application monitoring in production.

<h2>Technologies Used:</h2>

* [Python](https://www.python.org/)
* [Poetry](https://python-poetry.org/): Python dependency manager.
* [Django](https://www.djangoproject.com/): High-level open source Python web framework.
* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/): Frontend toolkit.
* [PostgresSQL](https://www.postgresql.org/): Powerful open source object-relational database system.
* [Rollbar](https://rollbar.com/): Error Logging & Tracking Service

<h2>Getting Started:</h2>

* Install the dependency management tool Poetry from https://python-poetry.org/docs/.
* Clone the repository with

```bash 
git clone https://github.com/saintodes/python-project-52.git
````

* Set up a virtual environment by running:

```shell
>> python -m venv venv
```

* Activate a virtual enviroment:

```shell 
source env/bin/activate
```

* Install PostgresSQL version 14 from https://www.postgresql.org/download/.
* Create a .env file in the project root folder containing the SECRET_KEY (for Django operation) and DATABASE_URL (link
  to your Postgres database).
  An example can be found in the env-example.env file.
* If the database is hosted on a PaaS service (e.g., render.com, railway.app, etc.) with a pre-created user and
  database, skip the next step.
* For a local setup, run the script, which reads the DATABASE_URL from the .env file and sets up the user and database.

```bash
./dev-build.sh
``` 

* Build the application using the script, which performs migrations and installs dependencies with Poetry.

```bash 
./build.sh
```

* To launch the server, use next command:

```shell 
make run
```