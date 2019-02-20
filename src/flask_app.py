
from flask import Flask, g, render_template

import config

app = Flask(__name__)

app.secret_key = config.FLASK_SECRET_KEY

