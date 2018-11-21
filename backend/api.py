from flask import Flask, request, jsonify
from flask_cors import CORS
from .turing_machine import TuringMachine
from .tables import *

app = Flask(__name__)
CORS(app)

tables = {
        "division": division_table,
        "equals": equals_table
    }


@app.route("/test")
def hello():
    print("API Functioning normally")
    return "Hello World!"


@app.route("/execute")
def execute():
    operation = request.args.get("operation")
    input = request.args.get("input").replace(" ", "B") + "B"

    t = TuringMachine(input, initial_state=">",
                      final_states=["FIM"],
                      transition_table=tables[operation])

    while not t.final():
        t.step()

    data = {
        "input_tape": input,
        "result_tape": t.get_tape(),
        "operation_list": t.operation_list
    }

    return jsonify(data)
