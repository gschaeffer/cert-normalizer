"""Flask configuration."""
from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

l_fmt = "[%(asctime)s] %(levelname)s [at %(module)s: %(lineno)d] %(message)s"
DICT_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            "format": l_fmt,
            "datefmt": "%Y-%b-%d %H:%M:%S %Z",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default",
        }
    },
    "root": {"level": "DEBUG", "handlers": ["console"]},
}


class Config:
    """Base config."""

    SECRET_KEY = "default_flask_secret_session_key"
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    KEY_FILE_DIR = "/tmp"


class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
