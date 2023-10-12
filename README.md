# Image Storage API

## Installation

To set up this image storage API, follow these steps:

1. Start the application using Docker Compose:

   ```shell
   docker-compose up
   ```

2. Apply database migrations inside the Docker container:

   ```shell
   docker-compose exec -it web bash
   python manage.py migrate
   ```

3. Create a superuser for the application:

   ```shell
   python manage.py createsuperuser
   ```

4. In order to use the API, assign a user tier to the admin user via the admin panel.

## Access URLs

You can access the following URLs for the API:

- [Home](http://127.0.0.1:8000/)
- [Login](http://127.0.0.1:8000/auth/login)
- [Upload](http://127.0.0.1:8000/upload)
- [Expiring Links](http://127.0.0.1:8000/expiring-link)
- [Admin Panel](http://127.0.0.1:8000/admin)

Enjoy using the Image Storage API!
