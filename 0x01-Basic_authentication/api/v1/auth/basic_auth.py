#!/usr/bin/env python3
""" BasicAuth module """

from api.v1.auth.auth import Auth
import base64
import binascii
from typing import TypeVar
from models.user import User


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
        """Returns the User instance based on the email and password.

        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.

        Returns:
            User: The User instance or None if the user is not found or the
            password is invalid.
        """
        # Return None if user_email or user_pwd is None or not a string
        if not user_email or not user_pwd:
            return None
        try:
            # Search for the user in the database
            user = User.search(attributes={'email': user_email})
        except Exception:
            return None
        # Return None if there is no user in the database with the given email
        if not user:
            return None
        # Get the first user from the search results
        user = user[0]
        # Return None if the password is invalid
        if not user.is_valid_password(user_pwd):
            return None
        # Return the user instance
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves user instance for a request """
        auth_header = self.authorization_header(request)
        b64_auth_header = self.extract_base64_authorization_header(auth_header)
        dec_header = self.decode_base64_authorization_header(b64_auth_header)
        user_email, user_pwd = self.extract_user_credentials(dec_header)
        return self.user_object_from_credentials(user_email, user_pwd)
