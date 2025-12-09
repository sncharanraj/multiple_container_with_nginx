from flask import Flask
app = Flask(__name__)

@app.route("/api2")
def home():
    return {"message": "Hello from Service B (Flask)!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
