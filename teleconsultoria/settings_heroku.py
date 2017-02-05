from teleconsultoria.settings import *
import dj_database_url

ALLOWED_HOSTS = ['teleconsultoria.herokuapp.com',]

DEBUG = False

db_from_env = dj_database_url.config()

DATABASES['default'].update(db_from_env)
