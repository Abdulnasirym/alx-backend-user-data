#!/usr/bin/env python3
""" A python module """


from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks ig a path requires authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """ Gets the authorization header from the request """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user """
        return None
