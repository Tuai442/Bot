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


@index.route("/_receive_name", methods=['GET', "POST"])
def _receive_name():
    name = request.get_json()
    print("=============== RECEIVED ===============")
    print(name)
    # Als begin letter hoofdletter is.
    if name[0].isupper():
        return jsonify(True)
    else:
        return jsonify(False)

@index.route("/_receive_age", methods=['GET', "POST"])
def _receive_age():
    age = request.get_json()
    print("=============== RECEIVED ===============")
    print(age)
    age = int(age)
    if age > 12 and age < 99:
        return jsonify(True)
    else:
        return jsonify("De leeftijd moet groter dan 12 en kleiner dan 99 zijn.")


@index.route("/_receive_all", methods=['GET', "POST"])
def _receive_all():
    name, age = request.get_json()
    print("=============== RECEIVED ===============")
    print(name, age)
    age = int(age)
    if name[0].isupper() and age > 12 and age < 99:
        print("ok")
        return jsonify(True)
    else:
        return jsonify("De naam begin niet met een hoofd letter of"
                       " de leeftijd moet groter dan 12 en kleiner dan 99 zijn.")


