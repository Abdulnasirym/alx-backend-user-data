#!/usr/bin/env python3
""" BasicAuth module """

from api.v1.auth.auth import Auth


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
