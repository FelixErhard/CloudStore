"""Minimal Flask API used for integration testing in CI."""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health")
def health():
    """Return a simple health response."""
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
    #asdfsdf
    #asdfasdf