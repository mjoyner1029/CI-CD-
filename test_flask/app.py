from flask import Flask, request

app = Flask(__name__)

@app.route('/sum')
def sum_numbers():
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    return str(num1 + num2)

if __name__ == '__main__':
    app.run(debug=True)
