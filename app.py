from flask import Flask
from flask_smorest import Api

from resources.items import blp as ItemBluePrint
from resources.store import blp as StoreBluePrint


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"

# OPEANAPI Doc: https://flask-smorest.readthedocs.io/en/latest/openapi.html
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"]  = "/"

# Laoding swagger UI http://localhost:5000/swagger-ui
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

# Resources created items and store
api.register_blueprint(ItemBluePrint)
api.register_blueprint(StoreBluePrint)

