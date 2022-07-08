#!/usr/bin/env python3
""" Route module - Get locale from request"""


from flask import Flask, request, render_template
from flask_babel import Babel
from os import getenv

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Babel configuration """
    LANGUAGES = ['en', 'fr']
    # these are the inherent defaults just btw
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# set the above class object as the configuration for the app
app.config.from_object('2-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET """
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> str:
    """ Determine best match for supported language """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
