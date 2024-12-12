from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.json
    height = data.get('height')  # mètres
    weight = data.get('weight')  # kg
    if not height or not weight:
        return jsonify({"error": "Height and weight are required"}), 400
    bmi = calculate_bmi(height, weight)
    return jsonify({"bmi": bmi}), 200

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.json
    height = data.get('height')  # cm
    weight = data.get('weight')  # kg
    age = data.get('age')       # age
    gender = data.get('gender') # homme ou femme
    if not height or not weight or not age or not gender:
        return jsonify({"error": "Height, weight, age, and gender are required"}), 400
    bmr = calculate_bmr(height, weight, age, gender)
    return jsonify({"bmr": bmr}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
