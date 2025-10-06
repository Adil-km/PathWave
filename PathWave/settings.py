from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------
# SECURITY
# ---------------------
SECRET_KEY = 'django-insecure-7+bc59s_&p8ij5@2o6($tkn)lo2=ck5!wen0t)ak+bh8!xj#xp'
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['localhost', '127.0.0.1',"https://demo-project-landing-page.vercel.app"]
if os.getenv('RENDER') == 'True':
    ALLOWED_HOSTS += ['pathwave.onrender.com']

# ---------------------
# INSTALLED APPS
# ---------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'UploadFile',
    'corsheaders',
]

# ---------------------
# MIDDLEWARE
# ---------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------------
# URL + WSGI
# ---------------------
ROOT_URLCONF = 'PathWave.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PathWave.wsgi.application'

# ---------------------
# DATABASES
# ---------------------
if os.getenv('RENDER') == 'True':
    print("#### connected to Render..............")
    DATABASES = {
        'default': dj_database_url.config(default=os.getenv("DATABASE_URL"), conn_max_age=600)
    }
else:
    print("#### connected to SQLite...............")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ---------------------
# AUTH PASSWORD VALIDATORS
# ---------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------------
# LANGUAGE / TIMEZONE
# ---------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------------
# STATIC FILES
# ---------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

# ---------------------
# MEDIA FILES (Uploads)
# ---------------------
if os.getenv('RENDER') == 'True':
    MEDIA_ROOT = '/tmp/media/' 
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# ---------------------
# DEFAULT PRIMARY KEY
# ---------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
