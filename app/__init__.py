import json
import logging
from logging.config import dictConfig

from flask import Flask, render_template
from flask.logging import default_handler

import config

from .modules import firestore

dictConfig(config.DICT_CONFIG)


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)

    # config
    cfg = "config.DevConfig" if app.config["DEBUG"] == True else "config.ProdConfig"
    app.logger.info(f"app config set to {cfg}")
    app.config.from_object(cfg)
    app.config.from_prefixed_env()

    with app.app_context():
        register_blueprints(app)
        initialize_extensions(app)
        configure_logging(app)
        register_error_handlers(app)

        configure_appsettings(app)
        set_logging_level(app, app.config.get("LOG_LEVEL"))
    return app


def register_blueprints(app):
    from .blueprints import root

    app.register_blueprint(root.root_bp)


def initialize_extensions(app):
    pass


def configure_logging(app):
    app.logger.removeHandler(default_handler)


def register_error_handlers(app):
    # app.register_error_handler(404, page_not_found)
    # app.register_error_handler(500, internal_server_error)
    # app.logger.info("error handlers set.")
    pass


def configure_appsettings(app):
    # app_settings['message']
    app_settings = firestore.get_config("members")

    if app_settings:
        error = False
        if "members" not in app_settings:
            logging.error(f"Key 'members' was not found in config_id 'members'")
            error = True

        if error == False:
            names = app_settings["members"]
    else:
        app.logger.warning("appsettings not found during init.")

    key_errors = {}
    for k, v in app_settings.items():
        try:
            app.config[k.upper()] = v
            # pprint(f'key: {k.upper()}, value: {app.config[k.upper()]}')
        except Exception as ex:
            key_errors[k] = v
            app.logger.error(
                f"""Error getting config keys.
                            {"".join(key_errors)}. {ex}"""
            )


def set_logging_level(app, level="INFO"):
    if level not in ["CRITICAL", "DEBUG", "ERROR", "INFO", "WARNING"]:
        level = "DEBUG"
    set_level = logging.getLevelName(level)
    app.logger.setLevel(set_level)


def page_not_found(e):
    return render_template("404.html"), 404


def internal_server_error(e):
    return render_template("500.html"), 500
