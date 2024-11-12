#!/usr/bin/env python3
""" BasicAuth module """

from api.v1.auth.auth import Auth
import base64
import binascii


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
