from flask import Flask, request, jsonify

from demography import analyze_member_demography, check_member_format

app = Flask(__name__)


@app.route("/api/analyze-demography", methods=["POST"])
def analyze_demography():
    data = request.get_json()
    if not isinstance(data, list):
        return jsonify({"error": "Expected a JSON array of members"}), 400

    if not check_member_format(data):
        return jsonify({"error": "Invalid format of member"}), 400

    result = analyze_member_demography(data)
    return jsonify(result), 200


if __name__ == '__main__':
    app.run()
