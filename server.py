#!/usr/bin/env python3

"""FormulaManager flask server"""

import yaml

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    """Index page"""
    return "Index page"


DATABASE = {
    "formula_name": "Test formula",
    "formula_list": ["TestFormula"],
    "system_data": {}
}


def load_layout(file_name="test_formula.yml"):
    """Load the formula layout from a yaml file"""
    with open(file_name) as layout_file:
        DATABASE["layout"] = yaml.load(layout_file)


@app.route("/testData")
def test_data():
    """Test formula"""
    load_layout()
    return jsonify(DATABASE)


@app.route("/save", methods=["POST"])
def save():
    """Save formula data"""
    DATABASE["system_data"] = request.get_json().get("content", {})
    print("== Save request:")
    print(DATABASE["system_data"])
    print("================")
    return jsonify(["Success!"])


if __name__ == "__main__":
    app.run(debug=True)
