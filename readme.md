# ALERT APP

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Usage](#usage)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Development Server](#running-the-development-server)
  - [Run in Docker](#run-in-docker)
- [Database](#database)
- [Testing](#testing)
- [Author](#author)


## Project Overview

This project is designed to facilitate the transmission of alarm messages to rescuers when an emergency call is received. It is developed using Django 5.0.2, GraphQL, and MongoDB. The project operates entirely through an API, with no graphical user interface. Users can send alarm messages to selected contacts, and all Create, Read, Update, and Delete operations on the model are accessible through the API.


## Technologies:

The most important technologies used in the project:

- Python 3.12
- Django 5.0.2
- GraphQL (graphene 3.3 and graphene-django 3.2.0)
- Pre-commit 3.6.2
- Twilio 8.13.0
- MongoDB (mongoengine 0.27.0 and graphene-mongo 0.4.2)
- Docker 24.0.5


## Usage

To use application you need to have user account in email service and sms service. This project using Sendgrid (email) and Twilio (sms).

## Features

- [Feature 1]: Send alarm message to contacts saved in database. User can send to API id-s of rescuers and message.
Application will send SMS and email to them.
- [Feature 1]: User can make all CRUD operations on RescueContacts - by using one api endpoint.

## Getting Started

Follow these steps to get your project up and running locally.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SzymKam/alert_app
   ```

2. Create a virtual environment and install poetry (optional but recommended):

   ```bash
    pip install poetry
    poetry env use python3.12
   ```

3. Install project dependencies:

   ```bash
    poetry install
   ```

### Configuration

Configure your project by setting up environment variables:

- SECRET_KEY - default is randomly generated
- DEBUG - in production set to False

Create local server of MongoDB, and set variables to connect:

- MONGODB_NAME - your mongodb database name
- MONGODB_HOST - your mongodb database host
- MONGODB_PORT - your mongodb database port (default=27017)

For sending emails to rescue users, please set connection to email service:

- EMAIL_HOST_PASSWORD - your email host user password
- EMAIL_HOST_USER - your email host_user
- DEFAULT_FROM_EMAIL - default email address

For sending SMS to rescuers, set variables to sms service (this project uses Twilio):

- TWILIO_ACCOUNT_SID - your twilio account sid
- TWILIO_AUTH_TOKEN - your twilio auth token
- TWILIO_PHONE_NUMBER - your twilio phone number

#### To help set local variables correctly, you can use ".env.dist" file. Copy this file as ".env" and set you variables values.


### Running the Development Server`

1. Start the development server:

```bash
cd src
poetry run python manage.py runserver
```

Your Django project should now be accessible at [http://localhost:8000/].


### Run in Docker

Project includes pre-made files to run docker containers:
Make sure you have installed and running Docker engine. To run project:

```bash
docker compose up --build
```

Your Django project should now be accessible at [http://localhost/].


## Database

Overview of the database models:

- [Model 1]: RescueContact - includes fields: first name and last name and contact information: phone number and
email address. Rest of fields are information about medical and technical qualifications of rescuer ex.: driver, navigator,
planner.


## Testing

To run the tests for this project, use the following command:

```bash
poetry run python manage.py test
```


## Author

SzymKam

https://github.com/SzymKam
