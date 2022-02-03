from flask import Flask
from app.routes.anime_routes import bp_anime

def init_app(app: Flask):
    app.register_blueprint(bp_anime)
