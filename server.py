#!/usr/bin/env python3

"""FormulaManager flask server"""

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
    "formula_list": ["TestFormula", "Other Formula"],
    "layout": {
        "MyTest": {
            "$type": "text",
            "$default": "default text"
        },
        "Group": {
            "$type": "group",
            "some-color": {
                "$type": "color"
            },
            "some-bool": {
                "$type": "boolean"
            },
            "pwd": {
                "$type": "password",
                "$visibleIf": "Group$some-bool == true"
            }
        }
    },
    "system_data": {}
}


@app.route("/testData")
def test_data():
    """Test formula"""
    return jsonify(DATABASE)
    # response = app.response_class(
    #     response=json.dumps(data),
    #     status=200,
    #     mimetype='application/json'
    # )
    # return response


@app.route("/save", methods=["POST"])
def save():
    """Save formula data"""
    DATABASE["system_data"] = request.get_json().get("content", {})
    print("Save request:")
    print(DATABASE["system_data"])
    return jsonify(["Success!"])


if __name__ == "__main__":
    app.run(debug=True)
