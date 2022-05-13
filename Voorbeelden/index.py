import json
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, Flask, Response

index = Blueprint("index", __name__,
                  template_folder='templates',
                  static_folder='static',
                  static_url_path='styles')

@index.route("/")
@index.route("/home", methods=['GET', "POST"])
def home():
    return render_template('test.html')



@index.route("/_receive_data", methods=['GET', "POST"])
def _receive_data():
    data = request.get_json()
    print("=============== RECEIVED ===============")
    print(data)
    # Als begin letter hoofdletter is.
    if data[0].isupper():
        return jsonify(True)
    else:
        return jsonify(False)

#     <script src="{{ url_for('index.static', filename='script/voorbeeld.js')}}"></script>