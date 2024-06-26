#!/usr/bin/env python3
""" Module showing Babel Implementation"""
from flask_babel import Babel
from flask import Flask, render_template, request, flash

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ Configuration Classfor babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """Renders a template showing Babel Implementation"""
    return render_template("3-index.html")


@babel.localeselector
def get_locale() -> str:
    """Picks language translation for a request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
