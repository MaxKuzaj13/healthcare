healthcare
==============================

healthcare

### Quick setup

> The next steps assume that conda is already installed

1 - <a name="step-1">Create a conda environment:</a>


```bash
conda create python=3.8 -n healthcare
```
2 - <a name="step-2">Activate the conda environment</a>

```bash
conda activate healthcare
```

3 - <a name="step-3">Install the project basic dependencies and development dependencies</a>

> Make sure you are inside the root project directory before executing the next commands.
>
> The root project directory is the directory that contains the `manage.py` file

On Linux and Mac

```bash
pip install -r requirements/local.txt
```

On Windows

```bash
pip install -r requirements\local.txt
```

4 - <a name="step-4">Configure the database connection string on the .env</a>

On Linux and Mac

```bash
cp env.sample.mac_or_linux .env
```

On Windows

```bash
copy env.sample.windows .env
```

Change the value of the variable `DATABASE_URL` inside the file` .env` with the information of the database we want to connect.

Note: Several project settings have been configured so that they can be easily manipulated using environment variables or a plain text configuration file, such as the `.env` file.
This is done with the help of a library called django-environ. We can see the formats expected by `DATABASE_URL` at https://github.com/jacobian/dj-database-url#url-schema. 

5 - <a name="step-5">Use the django-extension's `sqlcreate` management command to help to create the database</a>

On Linux:

```bash
python manage.py sqlcreate | sudo -u postgres psql -U postgres
```

On Mac:

```bash
python manage.py sqlcreate | psql
```

On Windows:

Since [there is no official support for PostgreSQL 12 on Windows 10](https://www.postgresql.org/download/windows/) (officially PostgreSQL 12 is only supported on Windows Server), we choose to use SQLite3 on Windows

6 - <a name="step-6">Run the `migrations` to finish configuring the database to able to run the project</a>


```bash
python manage.py migrate
```


### <a name="running-tests">Running the tests and coverage test</a>


```bash
coverage run -m pytest
```


## <a name="troubleshooting">Troubleshooting</a>

If for some reason you get an error similar to bellow, is because the DATABASE_URL is configured to `postgres:///healthcare` and because of it the generated `DATABASES` settings are configured to connect on PostgreSQL using the socket mode.
In that case, you must create the database manually because the `sqlcreate` is not capable to correctly generate the SQL query in this case.

```sql
ERROR:  syntax error at or near "WITH"
LINE 1: CREATE USER  WITH ENCRYPTED PASSWORD '' CREATEDB;
                     ^
ERROR:  zero-length delimited identifier at or near """"
LINE 1: CREATE DATABASE healthcare WITH ENCODING 'UTF-8' OWNER "";
                                                             ^
ERROR:  syntax error at or near ";"
LINE 1: GRANT ALL PRIVILEGES ON DATABASE healthcare TO ;
```



```sql
ERROR:  role "myuser" already exists
ERROR:  database "healthcare" already exists
GRANT
```

<a name="troubleshooting-delete-database">You can delete the database and the user with the commands below and then [perform step 5 again](#step-5).</a>

> :warning: **Be very careful here!**: The commands below erase data, and should only be executed on your local development machine and **NEVER** on a production server.


On Linux:

```bash
sudo -u postgres dropdb -U postgres --if-exists healthcare
sudo -u postgres dropuser -U postgres --if-exists myuser
```

On Mac:

```bash
dropdb --if-exists healthcare
dropuser --if-exists myuser
```


#USER 
## How use cookiecutter

Instalation 
- pip install --user cookiecutter
- python -m cookiecutter gh:feldroy/django-crash-starter
- cp env.sample.mac_or_linux .env
- pip install -r requirements/local.txt 



#PSQL

##Create
createdb healtcare -U postgres --password postgres
## SQL  

CREATE USER django_health WITH PASSWORD 'xyz123^dd2ded';
CREATE DATABASE django_health;
ALTER ROLE django_health SET client_encoding TO 'utf8';
ALTER ROLE django_health SET default_transaction_isolation TO 'read committed';
ALTER ROLE django_health SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE django_health TO django_health;

####OR 
python manage.py sqlcreate

you have:

CREATE USER postgres WITH ENCRYPTED PASSWORD 'postgres' CREATEDB;
CREATE DATABASE healtcare WITH ENCODING 'UTF-8' OWNER "postgres";
GRANT ALL PRIVILEGES ON DATABASE healtcare TO postgres;


## continuation
export DATABASE_URL=postgres://django_health:xyz123^dd2ded@127.0.0.1:5432/healtcare

python manage.py migrate     
python manage.py createsuperuser

## Translation
To make translation:

python manage.py makemessages --locale en
python manage.py makemessages --locale pl

To use translation:
add {% load i18n %} in files and add block {% blocktrans %} {% endblocktrans %} and in locale 
folder add translation. On the end add command <bash> python manage.py compilemessages </bash>
