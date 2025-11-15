import json
from flask import Flask, request
from typing import Text, Optional, Dict, Any

app = Flask(__name__)

# In-memory storage for user data
user_store: Optional[Dict[Text, Any]] = None


def get_current_user() -> Optional[Dict[Text, Any]]:
    """Extract current user details from in-memory storage."""
    return user_store


def store_user(user: Dict[Text, Any]) -> None:
    """Save user details to in-memory storage."""
    global user_store
    user_store = user


@app.route('/', methods=["GET"])
def greet():
    """Greet the user."""
    user = get_current_user()
    if user is not None:
        return "Hello, {}!".format(user.get("name"))
    else:
        return "Hello, unknown stranger!"


@app.route('/', methods=["POST"])
def save_name():
    """Change a user's details."""
    user = request.json
    store_user(user)
    return "I'll try to remember your name, {}!".format(user.get("name"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)