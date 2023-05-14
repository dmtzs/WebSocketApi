try:
    import os
    from flask import Flask
    import flask_authgen_jwt
    from dotenv import load_dotenv
except ImportError as e_imp:
    print(f"The following import ERROR occurred in {__file__}: {e_imp}")

# Definir la clave secreta para firmar el token
if os.path.exists("secret.env"):
    load_dotenv("secret.env")
else:
    print("No secret.env file found")
    raise SystemExit

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Configure Flask-Authgen-JWT to use in your Flask app
gen_auth = flask_authgen_jwt.GenJwt(json_body_token=True)
auth = flask_authgen_jwt.DecJwt()

from app import routes, error_handlers