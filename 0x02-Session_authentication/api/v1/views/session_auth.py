#!/usr/bin/env python3
""" Module of Session Auth views
"""
import os
from api.v1.views import app_views
from flask import request, jsonify
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def view_session_login() -> str:
    """ POST /api/v1/auth_session/login
    """
    email, password = request.form.get('email'), request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    User.load_from_file()
    users = User.search({"email": email})
    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    if not users[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    out = jsonify(users[0].to_json())
    out.set_cookie(os.getenv('SESSION_NAME'), auth.create_session(users[0].id))
    return out
