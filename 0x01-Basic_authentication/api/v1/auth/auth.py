#!/usr/bin/env python3
""" A python module """

from flask import request
from typing import List, TypeVar


class Auth:
    """ All authentication system implemented in this app"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks ig a path requires authentication"""
        if path is None:
            return True

        if not excluded_paths:
            return True

        normalized_path = path if path.endswith('/') else path + '/'

        if normalized_path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Gets the authorization header from the request """
        if request is None or 'Authorization' not in request.headers:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user """
        return None
