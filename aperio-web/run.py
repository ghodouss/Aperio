from flask import Flask, render_template, jsonify, request, send_file
from random import *
from flask_cors import CORS
import requests
from enhance_video import process_file

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/video', methods=['GET', 'POST'])
def process_video():
    files = request.files

    for key, value in files.items():
        value.save("/tmp/input.mp4")
        process_file("/tmp/input.mp4")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
