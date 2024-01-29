from flask import Flask
import shopify
import logging

from .env import API_KEY, API_SECRET
from . import routes

if not API_KEY or not API_SECRET:
    print("Please set SHOPIFY_API_KEY and SHOPIFY_API_SECRET")
    exit(1)

shopify.Session.setup(api_key=API_KEY, secret=API_SECRET)

app = Flask(__name__)

app.add_url_rule("/install", view_func=routes.install_route, methods=["GET"])
app.add_url_rule("/exchange", view_func=routes.exchange_token, methods=["GET"])

if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
