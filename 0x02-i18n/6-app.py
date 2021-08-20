#!/usr/bin/env python3
"""
setup a basic Flask app
create a single / route and an index.html template
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Union

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return 6-index.html template
    """
    return render_template('6-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    determine the best match with our supported languages
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            retun locale

    langHeader = request.headers.get('Accept-Language')
    if langHeader and langHeader in app.config['LANGUAGES']:
        return langHeader

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """
    returns a user dictionary or None if the ID cannot be found or if
    login_as was not passed
    """
    user = request.args.get('login_as')
    if user in users:
        return users[int(user)]
    else:
        None


@app.before_request
def before_request():
    """
    use get_user to find a user if any, and set it as a global on flask.g.user
    """
    g.user = get_user()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
