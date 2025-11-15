import json, os
from flask import Flask, request

app = Flask(__name__)
DATA_FILE = "/data/user.json"

def get_current_user():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE) as f:
                return json.load(f)
        except json.JSONDecodeError:
            return None
    return None

def store_user(user):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(user, f)

@app.route('/', methods=["GET"])
def greet():
    user = get_current_user()
    return f"Hello, {user.get('name') if user else 'unknown stranger'}!"

@app.route('/', methods=["POST"])
def save_name():
    user = request.json
    store_user(user)
    return f"I'll try to remember your name, {user.get('name')}!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)