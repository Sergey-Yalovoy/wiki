

# WiKi

![example](example.gif)

WiKi is a project based on **[django-wiki](https://github.com/django-wiki/django-wiki)** deployed in a docker container with a function to automatically convert Word (.docx) document to markdown. This project does not change the existing project, but only complements the upload attachments feature.

## Deploy project

To run the project, just run the command to run the build based on **gunicorn**

```bash
docker-compose up -d --build
```

To start the development environment, use:

```bash
docker-compose -f docker-compose-dev.yml up -d --build
```

Or you can create a python environment and run

```bash
python manage.py runserver 0.0.0.0:8000
```

in the ***docker-compose.yml*** file, you can uncomment the services responsible for **nginx** and run with it, otherwise you need to deploy your **ngixn** server instance to and configure routing

## Migrations and user creations

Connect to the container.

```bash
docker-compose exec wiki bash
```

Perform migration and create user. Everything is done as in a regular Django application.

```bash
python manage.py migrate
python manage.py createsuperuser
```

You can now open in your browser and create your first article.
