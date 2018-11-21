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
    operand1 = int(request.args.get("operand1"))
    operand2 = int(request.args.get("operand2"))

    operand1_string, operand2_string = "", ""

    for i in range(0, operand1):
        operand1_string += "*"
    for i in range(0, operand2):
        operand2_string += "*"

    input_tape = ">" + operand1_string + "B" + operand2_string + "B"

    t = TuringMachine(input_tape, initial_state=">",
                      final_states=["FIM"],
                      transition_table=tables[operation])

    while not t.final():
        t.step()

    data = {
        "input_tape": input_tape,
        "result_tape": t.get_tape(),
        "operation_list": t.operation_list
    }

    print(data)

    return jsonify(data)
