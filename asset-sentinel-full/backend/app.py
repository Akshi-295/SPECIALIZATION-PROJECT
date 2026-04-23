from flask import Flask, jsonify
from routes.alerts import alert_bp
from routes.accidents import accident_bp

app = Flask(__name__)
app.register_blueprint(alert_bp)
app.register_blueprint(accident_bp)

@app.route("/")
def home():
    return jsonify({"message": "Asset Sentinel API Running"})

if __name__ == "__main__":
    app.run(debug=True)
