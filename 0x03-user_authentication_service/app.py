#!/usr/bin/env python3
"""
This module sets up a basic flask app.
"""
from flask import Flask, jsonify, request, abort, redirect, url_for
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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ DELETE /sessions
    """
    user = AUTH.get_user_from_session_id(request.cookies.get('session_id'))
    if user:
        AUTH.destroy_session(user.id)
        return redirect(url_for('message'))
    abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """ GET /profile
    """
    user = AUTH.get_user_from_session_id(request.cookies.get('session_id'))
    if user:
        return jsonify({"email": user.email})
    abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """ POST /reset_password
    """
    try:
        reset_token = AUTH.get_reset_password_token(request.form.get('email'))
        return jsonify({"email": request.form.get('email'),
                        "reset_token": reset_token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """ PUT /reset_password
    """
    try:
        AUTH.update_password(request.form.get('reset_token'),
                             request.form.get('new_password'))
        return jsonify({"email": request.form.get('email'),
                        "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
