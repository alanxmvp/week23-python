from flask import Flask, jsonify
from sudoku import solve

app = Flask(__name__)


@app.route("/")
def hello():
    return f"Hello World"


@app.route("/test")
def test():
    return jsonify({"message": "hello world"})


@app.route("/users")
def users():
    return jsonify({"username": "john", "email": "john@john.com"})


@app.route("/public")
def public():
    return jsonify(
        {"id": 123, "locked": False, "name": "John", "roles": ["admin", "employee"]}
    )

@app.route('/sudoku', methods = ['POST'])
def sudoku():
    data = request.get_json()
    board = data["board"]
    result = solve(board)
    return jsonify({
        "board": result
    })


app.run(debug=True)
