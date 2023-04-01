from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

if __name__ == '__main__':
    app.run(port = int(os.environ.get("PORT", 5000)))
