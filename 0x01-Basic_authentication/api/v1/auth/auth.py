#!/usr/bin/env python3
from flask import Flask, request
from typing import List, TypeVar


class Auth():
    """ A class to return a boolean for path
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
