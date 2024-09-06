# app.py

from flask import Flask

app = Flask(__name__)

def calculate_sum(a, b):
    return a + b

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
