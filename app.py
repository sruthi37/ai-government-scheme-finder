from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load schemes database
with open("schemes.json", "r", encoding="utf-8") as file:
    data = json.load(file)

schemes = data["schemes"]


@app.route("/")
def home():
    return jsonify({
        "message": "AI Scheme Finder Backend Running"
    })


@app.route("/schemes")
def get_schemes():
    return jsonify(schemes)


@app.route("/match", methods=["POST"])
def match_schemes():

    user = request.json

    age = int(user.get("age", 0))
    income = int(user.get("income", 0))

    matched = []

    for scheme in schemes:

        eligibility = scheme.get("eligibility", {})

        age_min = eligibility.get("age_min", 0)

        age_max = eligibility.get("age_max")
        if age_max is None:
            age_max = 999

        income_max = eligibility.get("income_max")
        if income_max is None:
            income_max = 999999999

        if age_min <= age <= age_max and income <= income_max:

            matched.append({
                "id": scheme["id"],
                "name": scheme["name"],
                "category": scheme["category"],
                "benefit": scheme["benefit"]
            })

    return jsonify(matched)


if __name__ == "__main__":
    app.run(debug=True)