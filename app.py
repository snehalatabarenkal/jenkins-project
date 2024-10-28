from flask import Flask, request
import os

app = Flask(__name__)

# Hardcoded secret key
SECRET_KEY = "mysecretkey123"  # Vulnerability

# Unvalidated input
@app.route('/greet')
def greet_user():
    user = request.args.get('user')  # Code smell: no input validation
    return f"Hello, {user}"

@app.route('/')
def hello_world():
    return '''
    <html>
        <head>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                }
                h1 {
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <h1>This is DevOps Batch 2024!!!</h1>
        </body>
    </html>
    '''

# Dead code (function that is never called)
def unused_function():
    print("This function is not used.")

if __name__ == "__main__":
    # Debug mode enabled (security risk in production)
    app.run(host='0.0.0.0', port=5000, debug=True)  
