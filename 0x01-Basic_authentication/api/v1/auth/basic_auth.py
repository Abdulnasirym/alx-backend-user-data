#!/usr/bin/env python3
""" BasicAuth module """

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth classinheriting from Auth """
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        if authorization_header is None:
            return None

        elif not isinstance(authorization_header, str):
            return None

        elif not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(" ", 1)[1]
