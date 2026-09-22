# build 02be4c3bfd
# (auto) 99b76e
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
