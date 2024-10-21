from flask import Flask
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
