from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Hello Rajesh!</h1>
    <h2>This App is Running from GitHub Actions Pipeline</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)