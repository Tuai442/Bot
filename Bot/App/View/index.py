import json
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, Flask, Response
from time import sleep
import time

import os
import pprint

from View.Forms.strategy_form import FibonacciSetupForm, RsiSetupForm
from run import config, controller

index = Blueprint("index", __name__,
                 template_folder='templates',
                 static_folder='static',
                 static_url_path='styles')

@index.route("/home", methods=['GET', "POST"])
def home():
    symbols = config.available_symbols
    intervals = config.available_intervals
    return render_template('test.html', symbols=symbols, intervals=intervals)

# Bereikbaar via ajax__
@index.route("/_process_candles", methods=['POST'])
def _process_candles():
    data = request.get_json()
    controller.process_candle_data(data)
    graph = controller.get_graph()
    print("=============== GRAPH_INFO ==================")
    pprint.pprint(graph)
    return jsonify(graph)

@index.route("/_historical_candles", methods=['POST'])
def historical_candles():
    symbol, interval = request.get_json()
    h_candles = controller.get_historical_candles(symbol.upper(), interval)
    return jsonify(h_candles)

# LET OP: bij nieuwe strategiën toe te voegen moet de id van input field overeen komen.
@index.route("/_create_strategy", methods=['POST'])
def create_strategy():
    data = request.get_json()
    controller.create_simulation_agent(data)
    return jsonify()

@index.route("/")
@index.route("/simulation", methods=['GET', "POST"])
def simulation():
    return render_template("simulation.html", symbols=config.available_symbols, intervals=config.available_intervals,
                           fib_form=FibonacciSetupForm(), rsi_form=RsiSetupForm())


