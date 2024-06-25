By default Django is configured to use a SQLite database, which does not require setting up a server. An additional package - a MySQL client - will be needed to use a MariaDB database instead.

```
pip install mysqlclient
```

To set up the MariaDB database:

```
CREATE DATABASE your_database_name;
GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_username'@'localhost' IDENTIFIED BY 'your_password';
FLUSH PRIVILEGES;
```

The Django project's `settings.py` file will have to be updated to use the database connection.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',  # or the IP address of your database server
        'PORT': '3306',       # default port for MariaDB
    }
}
```

Creating, generating and applying database migrations should use the same methods as for a SQLite database:

```
python manage.py makemigrations  # to generate migrations
python manage.py migrate         # to apply migrations
```
