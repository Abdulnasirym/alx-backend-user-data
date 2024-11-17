#!/usr/bin/env python3
""" BasicAuth module """

from api.v1.auth.auth import Auth
import base64
import binascii
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth classinheriting from Auth """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract the base64 part of the Authorized header"""
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split("Basic ")[1].strip()

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes the Base64 string `base64_authorization_header` and
        returns the decoded value
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(
                base64_authorization_header,
                validate=True
            )
            return decoded.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extract user credentials"""
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user, password = decoded_base64_authorization_header.split(":", 1)
        return user, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ the class BasicAuth that returns
        the User instance based on his email and password.
        """
        if not all(map(lambda x: isinstance(x, str), (user_email, user_pwd))):
            return None

        try:
            user = User.search(attributes={'email': user_email})
        except Exception:
            return None

        if not user:
            return None:

        user = user[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user
