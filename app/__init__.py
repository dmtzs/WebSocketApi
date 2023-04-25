try:
    import os
    import toml
    import base64
    from flask import Flask
    from flask_pymongo import PyMongo
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

try:
    with open("credentials.toml", "r", encoding="utf8") as toml_file:
        asset = toml.load(toml_file)

    for decoded_cred, value in asset["database"].items():
        bytes_object = value.encode("utf8")
        base64_bytes = base64.b64decode(bytes_object)
        asset[decoded_cred] = base64_bytes.decode("utf8")
    asset = asset["database"]
except FileNotFoundError:
    asset = {}
    asset["db_username"] = os.environ.get("db_username")
    asset["db_password"] = os.environ.get("db_password")
    asset["db_name"] = os.environ.get("db_name")
    asset["collection"] = os.environ.get("collection")
    for decoded_cred, value in asset.items():
        bytes_object = value.encode("utf8")
        base64_bytes = base64.b64decode(bytes_object)
        asset[decoded_cred] = base64_bytes.decode("utf8")
    
mongo_uri = f'mongodb+srv://{asset["db_username"]}:{asset["db_password"]}@cluster0.agy4o.mongodb.net/{asset["db_name"]}'

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

app.config["MONGO_URI"] = mongo_uri
mongo = PyMongo(app)
db = mongo.db

from app import error_handlers, routes, admin_routes