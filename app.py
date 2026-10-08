from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Laundry Management System</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f6fc;
                text-align: center;
                padding: 50px;
            }

            .container {
                background: white;
                width: 600px;
                margin: auto;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            }

            h1 {
                color: #2c3e50;
            }

            h2 {
                color: #3498db;
            }

            .status {
                color: green;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Laundry Management System</h1>

            <h2>DevOps Pipeline Successfully Executed</h2>

            <p>Welcome to the Laundry Management System.</p>

            <p>Services:</p>

            <p>
                Washing &nbsp; | &nbsp;
                Dry Cleaning &nbsp; | &nbsp;
                Ironing
            </p>

            <p class="status">
                Application Deployed Successfully using Docker
            </p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)