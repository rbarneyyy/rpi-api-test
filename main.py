from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.get("/")
def main_page():
    return render_template("index.html"), 200

@app.get("/json")
def get_json():
    return jsonify({"test": "Hi!", "number": 1, "boolean": True}), 200

app.run(host="0.0.0.0", port=3000)