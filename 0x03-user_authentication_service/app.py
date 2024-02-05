#!/usr/bin/env python3
"""
This module sets up a basic flask app.
"""
from flask import Flask, jsonify, request, abort
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def message() -> str:
    """ GET /
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ POST /users
    """
    try:
        user = AUTH.register_user(request.form.get('email'),
                                  request.form.get('password'))
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /sessions
    """
    if AUTH.valid_login(request.form.get('email'),
                        request.form.get('password')):
        out = jsonify({"email": request.form.get('email'),
                       "message": "logged in"})
        out.set_cookie("session_id",
                       AUTH.create_session(request.form.get('email')))
        return out
    abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
