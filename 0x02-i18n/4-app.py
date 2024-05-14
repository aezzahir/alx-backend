#!/usr/bin/env python3
"""Get locale from request"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configuration class for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages. """
    if 'locale' in request.args and request.args['locale'] in Config.LANGUAGES:
        return request.args['locale']
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """Render the index.html template"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
