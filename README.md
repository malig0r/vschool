An app on django rest framework to digitalize the school documents.
Front-end is not built in, swagger provides basic overview of the endpoints.

Clone the repo, build a docker image by running.
$docker-compose up -d --build.
Access the docker internal terminal to then run
1) $python manage.py makemigrations
2) $python manage.py migrate
3) $python manage.py createsuperuser

Admin panel available through localhost:8080/admin/
Swagger documentation is available on the homepage.

Docker extracts postgres db and dependent django app.
As this is a pet-project, the setup must be adjusted for production use:
1) debug mode to be disabled
2) credentials to be extracted from the docker-compose file and vschool/settings.py
