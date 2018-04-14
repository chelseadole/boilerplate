"""Init script."""
from flask import Flask

app = Flask(__name__, static_url_path="/frontend/public", static_folder="../frontend/public")

from backend import routes
