def test_config(app):
    """
    GIVEN a Flask application
    WHEN log level is set
    THEN check the response is valid
    """

    assert len(app.config["SECRET_KEY"]) > 4
    # assert app.config["STATIC_FOLDER"] == 'static'
    # assert app.config["TEMPLATES_FOLDER"] == 'templates'
    # assert type(app.config["UPLOAD_EXTENSIONS"]) is list
    # assert len(app.config["UPLOAD_EXTENSIONS"]) >= 0
