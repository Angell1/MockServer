import os
import time
import json
from flask import jsonify
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/test', methods=["GET", "POST"])
def upload_test():
    return render_template("test.html")

#http://127.0.0.1:5000/show?filename=xxx


if __name__ == '__main__':
    app.run(debug=False)
