#!/usr/bin/env python3

"""FormulaManager flask server"""

from collections import OrderedDict

import json
import yaml

from flask import Flask, jsonify, request
from flask_cors import CORS


TEST_FORUMLA_FILE = "test_formula_partitions.yml"


app = Flask(__name__)
CORS(app)


def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)


@app.route("/")
def index():
    """Index page"""
    return "Index page"


DATABASE = {
    "formula_name": "Test formula",
    "formula_list": ["TestFormula"],
    "system_data": {}
}


def load_layout(file_name):
    """Load the formula layout from a yaml file"""
    with open(file_name) as layout_file:
        DATABASE["layout"] = ordered_load(layout_file)


@app.route("/testData")
def test_data():
    """Test formula"""
    load_layout(TEST_FORUMLA_FILE)
    # return jsonify(DATABASE) # Doesn't respect OrderedDicts
    response = app.response_class(
        response=json.dumps(DATABASE),
        status=200,
        mimetype="application/json"
    )
    return response


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
