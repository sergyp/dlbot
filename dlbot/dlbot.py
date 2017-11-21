#!/usr/bin/env python

from dlbot import default_settings
from flask import Flask
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(default_settings)
app.config.from_pyfile('dlbot.cfg', silent=True)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
