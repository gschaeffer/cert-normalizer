import copy
import os
import random
import string
from pprint import pprint

from flask import Blueprint
from flask import current_app as app
from flask import (
    jsonify,
    make_response,
    redirect,
    render_template,
    render_template_string,
    request,
    session,
    url_for,
)
from werkzeug.utils import secure_filename

from app.modules import normalizer
from app.modules.decorators import contenttype_json_required

root_bp = Blueprint(
    "root_bp", __name__, template_folder="templates", static_folder="static"
)


@root_bp.route("/", methods=["GET"])
def index():
    """base url."""
    return jsonify({"response": "reached /"})
    app.logger.info("appsettings refreshed.")


@root_bp.route("/", methods=["POST"])
@contenttype_json_required
def normalize():
    """normalize raw input content.

    export HEAD="Content-type: application/json"
    export PAYLOAD="{\"raw_content\": \"test\"}"
    export URL="localhost:8080/"
    $ curl -X POST -H $HEAD -d $PAYLOAD $URL

    $ curl -X POST -H $HEAD -d $PAYLOAD localhost:8080/
    """
    if "raw_content" not in request.json.keys():
        msg = {"message": "Payload data must contain 'raw_content' key."}
        return make_response(jsonify(msg), 401)
    raw_content = request.json["raw_content"]
    job_nbr = ""
    if "job_id" in request.json.keys():
        job_nbr = request.json["job_id"]

    try:
        n = normalizer.Normalizer(
            job_id=job_nbr,
            raw_content=raw_content,
            members=app.config.get("MEMBERS", []),
        )
        app.logger.info("normalize payload.")
        return make_response(jsonify({"response": n.data}), 200)
    except Exception as ex:
        msg = {"message": "Exception encountered.", "Exception": ex, "Type": type(ex)}
        return make_response(jsonify(msg), 401)
