#!/usr/bin/env python3
"""
setup a basic Flask app
create a single / route and an index.html template
"""

from flask import Flask, render_template
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    create Config class that has LANGUAGES class attribute equal to
    ["en", "fr"]
    use Config to set Babel’s default locale ("en") and timezone ("UTC")
    use that class as config for Flask app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index() -> str:
    """
    return 3-index.html template
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
