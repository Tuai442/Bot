from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, Flask, Response


from View.Forms.strategy_form import FibonacciSetupForm, RsiSetupForm
from run import config, controller

index = Blueprint("index", __name__,
                  template_folder='templates',
                  static_folder='static',
                  static_url_path='styles')


@index.route("/home", methods=['GET', "POST"])
def home():
    return render_template('test.html')