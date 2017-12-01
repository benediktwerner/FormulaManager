#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Index page"


test_formula = {
    "formula_name": "Test formula",
    "formula_list": ["TestFormula", "Other Formula"],
    "layout": {
        "MyTest": {
            "$type": "text",
            "$default": "default text"
        }
    }
}


@app.route("/testData")
def testData():
    return jsonify(test_formula)
    # response = app.response_class(
    #     response=json.dumps(data),
    #     status=200,
    #     mimetype='application/json'
    # )
    # return response


if __name__ == "__main__":
    app.run(debug=True)
