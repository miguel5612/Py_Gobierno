# app.py
"""Flask App Project."""

from flask import Flask, request, send_from_directory, flash, redirect, render_template, request, session, abort, jsonify
from sklearn.externals import joblib
import numpy as np
#import argparse
#import imutils
#import cv2


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index(name=None):
    return render_template('inicio.html', name=name)

@app.route('/dash', methods=['GET'])
def dashboard():
    return render_template('dash.html')

@app.route('/l', methods=['GET'])
def lol():
    return "lol"

@app.route('/favicon.ico')
def favicon():
    return 'no hay'

#Static folders
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


if __name__ == '__main__':
    app.run()