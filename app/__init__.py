try:
    from flask import Flask
except ImportError as e_imp:
    print(f"The following import ERROR occurred in {__file__}: {e_imp}")

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

from app import routes, error_handlers