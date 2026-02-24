from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CI/CD Flask App</title>

        <style>
            body {
                margin: 0;
                font-family: Arial, Helvetica, sans-serif;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: white;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .container {
                text-align: center;
                background: rgba(255,255,255,0.1);
                padding: 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                animation: fadeIn 1s ease-in-out;
            }

            h1 {
                font-size: 40px;
                margin-bottom: 10px;
            }

            h2 {
                font-weight: normal;
                color: #e0e0e0;
            }

            .badge {
                margin-top: 20px;
                padding: 10px 20px;
                background: #00c6ff;
                border-radius: 25px;
                display: inline-block;
                font-weight: bold;
            }

            button {
                margin-top: 25px;
                padding: 12px 25px;
                border: none;
                border-radius: 25px;
                background: #ff7e5f;
                color: white;
                font-size: 16px;
                cursor: pointer;
                transition: 0.3s;
            }

            button:hover {
                background: #feb47b;
                transform: scale(1.05);
            }

            @keyframes fadeIn {
                from {opacity: 0; transform: translateY(20px);}
                to {opacity: 1; transform: translateY(0);}
            }
        </style>
    </head>

    <body>

        <div class="container">
            <h1>🚀 Hello !!!</h1>
            <h2>Flask App Deployed using GitHub Actions CI/CD Pipeline</h2>

            <div class="badge">
                ✅ Build Successful | ✅ Deployment Active
            </div>

            <br>

            <button onclick="showMessage()">
                Check Pipeline Status
            </button>
        </div>

        <script>
            function showMessage() {
                alert("🎉 GitHub Actions Pipeline is Running Successfully!");
            }
        </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)