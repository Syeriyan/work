from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask App is Running Successfully ✅"

@app.route("/time")
def time():
    return f"Server Time: {datetime.datetime.now()}"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
