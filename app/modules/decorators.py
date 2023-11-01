import functools

from flask import Flask, jsonify, make_response, request


def contenttype_json_required(f):
    """Validates that the request has a Content-Type header with application/json."""

    @functools.wraps(f)
    def decorator(*args, **kwargs):
        content_type = request.headers.get("Content-Type")
        if content_type != "application/json":
            return make_response(
                jsonify({"message": "Content-Type header must be json."}), 401
            )
        return f(*args, **kwargs)

    return decorator


def token_required(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        token = None
        # ensure the jwt-token is passed with the headers
        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        if not token:  # throw error if no token provided
            return make_response(jsonify({"message": "A valid token is missing!"}), 401)
        try:
            # decode the token to obtain user public_id
            # data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            # current_user = User.query.filter_by(public_id=data["public_id"]).first()
            pass
        except:
            return make_response(jsonify({"message": "Invalid token!"}), 401)
        # Return the user information attached to the token
        # return f(current_user, *args, **kwargs)
        return f(None, *args, **kwargs)

    return decorator
