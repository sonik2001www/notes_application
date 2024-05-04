# Notes Application

## Overview

This project is aimed at developing a web application for note-taking. It allows users to create, view, edit, archive, and delete notes, as well as sort and filter them by various criteria.

## Key Features

- Adding, viewing, editing, archiving, and deleting notes.
- Ability to add categories for notes, which can be selected from existing ones or created anew.
- Sorting and filtering notes by different criteria.
- User authentication and identification.
- Sending email notifications for registration confirmation.
- Ownership of notes, automatically assigned to authenticated users upon note creation.
- Control over note creation and update timestamps.
- Application of templates for styling the user interface.

## Technical Details

- Django is used for backend development.
- PostgreSQL serves as the database.
- Allauth library is utilized for user authentication and identification.
- CI/CD setup with GitHub Actions, running Flake8 on each pull request to the `main` branch.
- Docker containers for convenient deployment and project management.
- Web-based admin interface provided by PGAdmin for database administration.

## Additional Steps to Run the Project

1. Download and install Docker from [the official website](https://www.docker.com/get-started).
2. Create `.env` and `secure.ini` files with the required configurations. See below for the format.

`secure.ini`
~~~
[settings] ; Django settings
secret_key=django-insecure-lbp6zcm*g08km@ter_g+ ; Django secret key
debug=True ; Debug mode (enabled)

client_id=****** ; Google client ID
secret=****** ; Google client secret
email_host_user=****** ; Email for sending notifications
email_host_password=****** ; two-factor password for email authentication

[database] ; Database settings
db_name=notes
db_user=root
db_host=localhost
db_port=5432
db_pass=1234

~~~

`.env`
~~~
; Django Super User credentials
USERNAME=admin
EMAIL=admin@gmail.com
DJANGO_SUPERUSER_PASSWORD=admin

; PostgreSQL settings
POSTGRES_HOST=db
POSTGRES_DB=notes
POSTGRES_USER=root
POSTGRES_PASSWORD=1234
POSTGRES_PORT=5432

; PGAdmin User credentials
PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=root
~~~

3. Obtain the Google Client ID and Secret Key for Google authentication from [Google Developers Console](https://console.developers.google.com/).
4. Define your email credentials for sending confirmation and other emails.
5. Enable two-factor authentication for your email and obtain the password.
6. Insert the obtained data into the respective files.
7. Run the project build and containers using the following commands:

~~~
docker-compose up
~~~

8. To visit the application notes, you can follow the link [http://0.0.0.0:8000/note/](http://0.0.0.0:8000/note/)

